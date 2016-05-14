from SCons.Script import *

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
