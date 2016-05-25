import copy     # For some reason importing this does not work
import os

from SCons.Script import *
import scons_utils
import setupTools

def buildCmake(env, output, sources, cmakeRootDir, buildDir, cmakeOptions, outputAfterCmakeBuild):
    return env.Command(output, sources, 
    [
        'echo "Building ' + output + '"',
        'mkdir -p ' + buildDir,
        'cmake -B' + buildDir + ' ' + '-H' + cmakeRootDir +' ' + 
            '-DCMAKE_BUILD_TYPE=Release ' +
            scons_utils.listToString(cmakeOptions, ' ') +
            '-DCMAKE_C_COMPILER=' + env['CC'] + ' ' +
            '-DCMAKE_CXX_COMPILER=' + env['CXX'],
        'make -C' + buildDir + ' -j',
        'cp ' + buildDir + '/' + outputAfterCmakeBuild + ' $TARGET'
    ])

def generateIncludeUsageRequirementName(libName):
    return 'LIB_' + libName.upper() + '_INCLUDES'

def createIncludeUsageRequirement(env, libName, includes):
    lib_include_requirements_name = generateIncludeUsageRequirementName(libName)

    if lib_include_requirements_name in env: 
        env[lib_include_requirements_name].extend(includes)
    else:
        env[lib_include_requirements_name] = includes

def addIncludeUsageRequirement(env, lib, toAdd):
    lib_include_requirements_name = generateIncludeUsageRequirementName(lib)
    if lib_include_requirements_name in env: 
        toAdd.extend(env[lib_include_requirements_name])

def createUnittest(env, name, sources, includes, libs, libs_path):
    env_unittest = env.Clone()
    libs_unittest = copy.deepcopy(libs)

    libs_unittest.extend(env['LIB_UNITTEST'])
    libs_unittest.extend(env['STD_LIBS'])

    env_unittest['CPPPATH'].extend(includes)
    env_unittest['CPPPATH'].append(env['ROOT_DIR'] + '/3rdparty/Catch/include')

    for lib in libs:
        addIncludeUsageRequirement(env_unittest, lib, env_unittest['CPPPATH'])

    target = env_unittest.Program(name, sources, LIBS=libs_unittest, LIBPATH=libs_path)
    installed_bin = env.Install("{bin_dir}".format(bin_dir=env['UNITTEST_BIN_DIR']), target)
    env.Alias(name, installed_bin)
    env.Alias("unittests", installed_bin)
    return installed_bin

def createBenchmark(env, name, sources, includes, libs, libs_path, TEMPS = []):
    env_benchmark = env.Clone()
    libs_benchmark = copy.deepcopy(libs)

    libs_benchmark.extend(env['LIB_BENCHMARK'])
    libs_benchmark.extend(env['STD_LIBS'])

    env_benchmark['CPPPATH'].extend(includes)

    for lib in libs:
        addIncludeUsageRequirement(env_benchmark, lib, env_benchmark['CPPPATH'])

    target = env_benchmark.Program(name, sources, LIBS=libs_benchmark, LIBPATH=libs_path)
    installed_bin = env.Install("{bin_dir}".format(bin_dir=env['BENCHMARK_BIN_DIR']), target)
    env.Alias(name, installed_bin)
    env.Alias("benchmarks", installed_bin)

    targetList = [installed_bin]

    # Create temps
    for temp in TEMPS:
        if temp == '.s' or temp == '.S':
            asm_files = createAssembler(env, name, sources, includes, libs, libs_path)
            targetList.append(asm_files)

    return targetList

def createAssembler(env, name, sources, includes, libs, libs_path):
    env_benchmark = env.Clone()

    env_benchmark['CPPPATH'].extend(includes)
    setupTools.stopAtAssembler(env_benchmark)

    for lib in libs:
        addIncludeUsageRequirement(env_benchmark, lib, env_benchmark['CPPPATH'])

    # Build target sources
    targets = []
    for source in sources:
        targetFile = os.path.splitext(source.rstr())[0]+'.s'
        target = env_benchmark.StaticObject(targetFile, source )
        env.Alias(name, target)
        env.Alias("benchmarks", target)

    return target

def createLib(env, name, sources, includes, includeUsageRequirements):
    createIncludeUsageRequirement(env, name, includeUsageRequirements)

    env_lib = env.Clone()
    env_lib['CPPPATH'].extend(includes)

    lib = env_lib.Library(name, sources)
    installed_lib = env.Install("{libs_dir}".format(libs_dir=env['LIBS_DIR']), lib)
    env.Alias(name, installed_lib)
    env.Alias('buildLibs', installed_lib)
