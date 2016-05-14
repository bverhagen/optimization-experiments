from SCons.Script import *

OPTIMIZATION_LEVEL_0 = 0
OPTIMIZATION_LEVEL_1 = 1
OPTIMIZATION_LEVEL_2 = 2
OPTIMIZATION_LEVEL_3 = 3
OPTIMIZATION_LEVEL_DEBUG = OPTIMIZATION_LEVEL_0

WARNING_LEVEL_NONE = 0
WARNING_LEVEL_SOME = 1
WARNING_LEVEL_ALL = 2

CXX_VERSION_03 = 0
CXX_VERSION_11 = 1

MULTI_THREADING_OFF = 0
MULTI_THREADING_PTHREAD = 1
MULTI_THREADING_OPENMP = 2

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

def getStdLibs(compiler):
    return list(['rt', 'm', 'dl', 'stdc++'])

def enableOptimization(env, optimizationLevel = OPTIMIZATION_LEVEL_0):
    if env['COMPILER_FAMILY'] == 'gcc' or env['COMPILER_FAMILY'] == 'clang':
        if optimizationLevel is OPTIMIZATION_LEVEL_0:
            env['CPPFLAGS'].append('-O0')
        elif optimizationLevel is OPTIMIZATION_LEVEL_1:
            env['CPPFLAGS'].append('-O1')
        elif optimizationLevel is OPTIMIZATION_LEVEL_2:
            env['CPPFLAGS'].append('-O2')
        elif optimizationLevel is OPTIMIZATION_LEVEL_3:
            env['CPPFLAGS'].append('-O3')
        else:
            print('Warning: optimization level ' + optimizationLevel + ' not supported')

def enableDebuggingSymbols(env):
    if env['COMPILER_FAMILY'] == 'gcc' or env['COMPILER_FAMILY'] == 'clang':
        env['CPPFLAGS'].append('-g')

def enableWarnings(env, warningLevel = WARNING_LEVEL_ALL):
    if env['COMPILER_FAMILY'] == 'gcc' or env['COMPILER_FAMILY'] == 'clang':
        if warningLevel >= WARNING_LEVEL_SOME:
            env['CPPFLAGS'].append('-Wall')
        if warningLevel >= WARNING_LEVEL_ALL:
            env['CPPFLAGS'].extend(['-Wextra', '-Wshadow',  '-Wpointer-arith', '-Wcast-qual'])

def enableCxxVersion(env, cxxVersion = CXX_VERSION_03):
    if env['COMPILER_FAMILY'] == 'gcc' or env['COMPILER_FAMILY'] == 'clang':
        if cxxVersion == CXX_VERSION_11:
            env['CPPFLAGS'].append('-std=c++11')

def enableMultiThreading(env, multiThreading = MULTI_THREADING_OFF):
    if env['COMPILER_FAMILY'] == 'gcc' or env['COMPILER_FAMILY'] == 'clang':
        if multiThreading == MULTI_THREADING_PTHREAD:
            env['CPPFLAGS'].append(['-pthread'])
        elif multiThreading == MULTI_THREADING_OPENMP:
            env['CPPFLAGS'].append(['-fopenmp'])
            env['LINKFLAGS'].append(['-fopenmp'])

def enableWarningAsError(env):
    if env['COMPILER_FAMILY'] == 'gcc' or env['COMPILER_FAMILY'] == 'clang':
        env['CPPFLAGS'].append('-Werror')
