#!/usr/bin/python

from ..util.util import *

def runTarget(target, mode, buildDir, profileMethod, valgrind, suffix = ''):
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
        if profileMethod == 'none':
            pass
        elif profileMethod == 'perf':
            outputFile = buildDir + '/perf.data'
            cmd.extend(['perf', 'record', '-o', outputFile]) 
        else:
            print('Invalid profiling method:' + profileMethod) 
            return False

        cmd.extend([buildDir + '/' + target + suffix])
    retCode = executeInShell(cmd)
    if profileMethod == 'perf':
        viewCmd = ['perf', 'report', '-i', outputFile] 
        return executeInShell(viewCmd)
    else:
        return retCode

def runUnittest(target, mode, compiler, profileMethod, valgrind):
    buildDir = getUnittestDir(mode, compiler)
    runTarget(target, mode, buildDir, profileMethod, valgrind, '-unittest')

def runPerformanceTest(target, mode, compiler, profileMethod, valgrind):
    buildDir = getPerformancetestDir(mode, compiler)
    runTarget(target, mode, buildDir, profileMethod, valgrind, '-benchmark')

def runner(targets, mode, runTargets, compiler, profileMethod, valgrind):
    for target in targets:
        for runTarget in runTargets:
            if(runTarget == 'unittest'):
                runUnittest(target, mode, compiler, profileMethod, valgrind)
            elif(runTarget == 'performance'):
                runPerformanceTest(target, mode, compiler, profileMethod, valgrind)
            elif(runTarget == 'all'):
                runUnittest(target, mode, compiler, profileMethod, valgrind)
                runPerformanceTest(target, mode, compiler, profileMethod, valgrind)
            else:
                print("Invalid run target!")
                return False
    return True
