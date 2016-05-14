import copy     # For some reason importing this does not work

from SCons.Script import *

def listToString(list, separator):
    return separator.join(list)

def buildCmake(env, output, sources, cmakeRootDir, buildDir, cmakeOptions, outputAfterCmakeBuild):
    return env.Command(output, sources, 
    [
        'echo "Building ' + output + '"',
        'mkdir -p ' + buildDir,
        'cmake -B' + buildDir + ' ' + '-H' + cmakeRootDir +' ' + 
            '-DCMAKE_BUILD_TYPE=Release ' +
            listToString(cmakeOptions, ' ') +
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

    for lib in libs:
        addIncludeUsageRequirement(env_unittest, lib, env_unittest['CPPPATH'])

    target = env_unittest.Program(name, sources, LIBS=libs_unittest, LIBPATH=libs_path)
    installed_bin = env.Install("{bin_dir}".format(bin_dir=env['UNITTEST_BIN_DIR']), target)
    env.Alias(name, installed_bin)
    env.Alias("unittests", installed_bin)
    return installed_bin

def createBenchmark(env, name, sources, includes, libs, libs_path):
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
    return installed_bin

def createLib(env, name, sources, includes, includeUsageRequirements):
    createIncludeUsageRequirement(env, name, includeUsageRequirements)

    env_lib = env.Clone()
    env_lib['CPPPATH'].extend(includes)

    lib = env_lib.Library(name, sources)
    installed_lib = env.Install("{libs_dir}".format(libs_dir=env['LIBS_DIR']), lib)
    env.Alias(name, installed_lib)
    env.Alias('buildLibs', installed_lib)
