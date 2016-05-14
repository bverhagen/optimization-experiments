import copy     # For some reason importing this does not work

from SCons.Script import *


x64_compiler_path = Dir('/usr/bin').abspath
armv6_compiler_path = Dir('toolchains/arm-bcm2708hardfp-linux-gnueabi/bin').abspath

map_c_to_cxx = {
    'gcc' : 'g++',
    'clang' : 'clang++'
}

map_arch_to_toolchain_path = {
    '' : x64_compiler_path,
    'arm-bcm2708hardfp-linux-gnueabi-' : armv6_compiler_path
}

def listToString(list, separator):
    return separator.join(list)

def setupToolchain(env, compiler, toolchainPrefix = None, toolchainPath = None):
    toolchain = ''
    compilerName = ''
    if toolchainPath:
        toolchain = toolchain + toolchainPath + '/'

    if toolchainPrefix:
        toolchain = toolchain + toolchainPrefix + '-'
        compilerName = toolchainPrefix + '-'

    # Define generally available environment variables
    env['COMPILER_NAME'] = compilerName + compiler
    env['COMPILER_FAMILY'] = compiler
    env['CC'] = toolchain + compiler

    if compiler == 'gcc':
        env['CXX'] = toolchain + 'g++'
        env['AR'] = toolchain + 'ar' 
        env['AS'] = toolchain + 'as' 
        env['LD'] = toolchain + 'ld'
        env['NM'] = toolchain + 'nm' 
        env['STRIP'] = toolchain + 'strip' 

    elif compiler == 'clang':
        env['CXX'] = toolchain + 'clang++'

    print("Toolchain: " + toolchain)
    print("C Compiler: " + env['CC'])
    print("CXX Compiler: " + env['CXX'])


def buildCmake(env, output, sources, cmakeRootDir, buildDir, cmakeOptions, outputAfterCmakeBuild):
    return env.Command(output, sources, 
    [
        'echo "Building ' + output + '"',
        'mkdir -p ' + buildDir,
        'cmake -B' + buildDir + ' ' + '-H' + cmakeRootDir +' ' + 
            listToString(cmakeOptions, ' ') +
            '-DCMAKE_C_COMPILER=' + env['CC'] + ' ' +
            '-DCMAKE_CXX_COMPILER=' + env['CXX'],
        'make -C' + buildDir + ' -j',
        'cp ' + buildDir + '/' + outputAfterCmakeBuild + ' $TARGET'
    ])

def generateIncludeUsageRequirementName(lib):
    return 'LIB_' + lib.upper() + '_INCLUDES'

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
    installed_bin = env.Install("{bin_dir}".format(bin_dir=env['BIN_DIR']), target)
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
    installed_bin = env.Install("{bin_dir}".format(bin_dir=env['BIN_DIR']), target)
    env.Alias(name, installed_bin)
    env.Alias("benchmarks", installed_bin)
    return installed_bin
