#!/usr/bin/python

from ..util.util import *

def runTarget(target, mode, buildDir, valgrind, suffix = ''):
    if(not target or target == 'all'):
        files = getAllFiles(buildDir)
        for entry in files:
            if not runTarget(entry, mode, buildDir, valgrind):
                return False
        return True
    else:
        cmd = []
        if valgrind:
            cmd.extend(['valgrind', '--tool=memcheck'])
        cmd.extend([buildDir + '/' + target + suffix])
    return executeInShell(cmd)

def runUnittest(target, mode, compiler, valgrind):
    buildDir = getUnittestDir(mode, compiler)
    runTarget(target, mode, buildDir, valgrind, '-unittest')

def runPerformanceTest(target, mode, compiler, valgrind):
    buildDir = getPerformancetestDir(mode, compiler)
    runTarget(target, mode, buildDir, valgrind, '-benchmark')

def runner(targets, mode, runTargets, compiler, valgrind):
    for target in targets:
        for runTarget in runTargets:
            if(runTarget == 'unittest'):
                runUnittest(target, mode, compiler, valgrind)
            elif(runTarget == 'performance'):
                runPerformanceTest(target, mode, compiler, valgrind)
            elif(runTarget == 'all'):
                runUnittest(target, mode, compiler, valgrind)
                runPerformanceTest(target, mode, compiler, valgrind)
            else:
                print("Invalid run target!")
                return False
    return True
