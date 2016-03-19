#!/usr/bin/python

from ..util.util import *

def runTarget(target, buildDir, valgrind, suffix = ''):
    if(not target or target == 'all'):
        files = getAllFiles(buildDir)
        for entry in files:
            if not runTarget(entry, buildDir, valgrind):
                return False
        return True
    else:
        cmd = []
        if valgrind:
            cmd.extend(['valgrind', '--tool=memcheck'])
        cmd.extend([buildDir + '/' + target + suffix])
    return executeInShell(cmd)

def runUnittest(target, mode, valgrind):
    buildDir = getUnittestDir(mode)
    runTarget(target, buildDir, valgrind, '-unittest')

def runPerformanceTest(target, mode, valgrind):
    buildDir = getPerformancetestDir(mode)
    runTarget(target, buildDir, valgrind, '-performance')

def runner(targets, mode, runTargets, valgrind):
    for target in targets:
        for runTarget in runTargets:
            if(runTarget == 'unittest'):
                runUnittest(target, mode, valgrind)
            elif(runTarget == 'performance'):
                runPerformanceTest(target, mode, valgrind)
            elif(runTarget == 'all'):
                runUnittest(target, mode, valgrind)
                runPerformanceTest(target, mode, valgrind)
            else:
                print("Invalid run target!")
                return False
    return True
