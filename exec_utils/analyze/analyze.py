#!/usr/bin/python

from ..util.util import *
from ..buildSystem.buildSystem import *

def analyzeClang(mode, target, verbose):
    return buildBuildSystem(target, mode, 'target', 'CC', verbose, False, prependCommand = ['scan-build', '-o', 'build/clang-static-analyze'])

def analyzeCppcheck(target, verbose):
    binary_name = 'cppcheck'
    if not isInstalled(binary_name):
        print('Please install ' + binary_name + ' or add it to your path.')

    includes = getAllDirsThatContainPattern(getSrcDir(), '.h')

    targetDir = getSrcDir(target)

    cmd = [binary_name]
    cmd.append('--enable=all')
    cmd.append('--std=c++11')
    cmd.append('--force')
    cmd.append('--error-exitcode=1')
    if verbose:
        cmd.append('--verbose')
    else:
        cmd.append('-q')

    for include in includes:
        cmd.append('--include=' + include)

    cmd.append(targetDir)
#    cmd.append('--check-config')
    retValue = isSuccess(executeInShell(cmd))
    if(retValue):
        print('Cppcheck did not find major issues.')
    else:
        print('Cppcheck found major issues.')
    return retValue

def analyzeCpplint(target, verbose):
    binary_name = 'cpplint'
    if not isInstalled(binary_name):
        print('Please install ' + binary_name + ' or add it to your path.')

    cmd = [binary_name]
    cmd.append('--filter=-legal/copyright,-whitespace/parens,-build/include,-whitespace/line_length,-runtime/references')
    cmd.append('src/simd-and/src/benchmark-simd-and-vector.cpp')
    return isSuccess(executeInShell(cmd))

def analyzeBuildSystem(method, mode, target, verbose):
    if method == 'clang':
        return analyzeClang(mode, target, verbose)
    if method == 'cppcheck':
        return analyzeCppcheck(target, verbose)
    if method == 'cpplint':
        return analyzeCpplint(target, verbose)
