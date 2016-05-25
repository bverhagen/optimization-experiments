from SCons.Script import *
from compilerEnumerations import *
import scons_utils
import re
import os

import gcc
import clang

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
        env['SETUPCONFIG_TOOLCHAIN'] = gcc.Gcc(env, toolchain)

    elif compiler == 'clang':
        env['SETUPCONFIG_TOOLCHAIN'] = clang.Clang(env, toolchain)

    print("Toolchain: " + toolchain)
    print("C Compiler: " + env['CC'])
    print("CXX Compiler: " + env['CXX'])

def getStdLibs(env, compiler):
    return env['SETUPCONFIG_TOOLCHAIN'].getStdLibs(compiler)

def enableOptimization(env, optimizationLevel = OPTIMIZATION_LEVEL_0):
    env['SETUPCONFIG_TOOLCHAIN'].enableOptimization(env, optimizationLevel)

def enableDebuggingSymbols(env):
    env['SETUPCONFIG_TOOLCHAIN'].enableDebuggingSymbols(env)

def enableWarnings(env, warningLevel = WARNING_LEVEL_ALL):
    env['SETUPCONFIG_TOOLCHAIN'].enableWarnings(env, warningLevel)

def enableCxxVersion(env, cxxVersion = CXX_VERSION_03):
    env['SETUPCONFIG_TOOLCHAIN'].enableCxxVersion(env, cxxVersion)

def enableMultiThreading(env, multiThreading = MULTI_THREADING_OFF):
    env['SETUPCONFIG_TOOLCHAIN'].enableMultiThreading(env, multiThreading)

def enableWarningAsError(env):
    env['SETUPCONFIG_TOOLCHAIN'].enableWarningAsError(env)

def saveTemps(env):
    env['SETUPCONFIG_TOOLCHAIN'].saveTemps(env)

def stopAtAssembler(env):
    env['SETUPCONFIG_TOOLCHAIN'].stopAtAssembler(env)

class Submodule:
    def __init__(self, name, commitHash):
        self.name = name
        self.commitHash = commitHash

def writeSubmoduleCommit(destinationFile, commit):
    print(destinationFile)
    with open(destinationFile, 'w') as f:
        f.write(commit)

def checkSubmodules(buildDir):
    cmd = ['git', 'submodule', 'status']
    out, err = scons_utils.getShellOutput(cmd)
    for line in out.splitlines():
        parts = line.strip().split(' ')
        commitHash = parts[0]
        if commitHash[0] == '-':
            commitHash = commitHash[1:]
        name = parts[1]

        submodule = Submodule(name, commitHash)
        destinationFile = submodule.name + '.commit'
        if os.path.isfile(destinationFile):
            with open(destinationFile, 'r') as f:
                if f.read() != submodule.commitHash:
                    # Means the commit has changed
                    writeSubmoduleCommit(destinationFile, submodule.commitHash)
        else:
            writeSubmoduleCommit(destinationFile, submodule.commitHash)
