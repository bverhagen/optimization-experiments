#!/usr/bin/python

from ..util.util import *

def runTarget(target, buildDir, suffix = ''):
    if(not target or target == 'all'):
        files = getAllFiles(buildDir)
        for entry in files:
            if not runTarget(entry, buildDir):
                return False
        return True
    else:
        cmd = [buildDir + '/' + target + suffix]
    return executeInShell(cmd)

def runUnittest(target, mode):
    buildDir = getUnittestDir(mode)
    runTarget(target, buildDir, '-unittest')

def runPerformanceTest(target, mode):
    buildDir = getPerformancetestDir(mode)
    runTarget(target, buildDir, '-performance')

def runner(targets, mode, runTargets):
    for target in targets:
        for runTarget in runTargets:
            if(runTarget == 'unittest'):
                runUnittest(target, mode)
            elif(runTarget == 'performance'):
                runPerformanceTest(target, mode)
            elif(runTarget == 'all'):
                runUnittest(target, mode)
                runPerformanceTest(target, mode)
            else:
                print("Invalid run target!")
                return False
    return True
