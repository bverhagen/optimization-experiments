#!/usr/bin/python

from ..util.util import *
from ..filter.filterchain import FilterChain
from ..filter.valgrindMemcheck import ValgrindMemcheck
from ..filter.runUnitTest import RunUnittest
from ..filter.runPerformanceTest import RunPerformancetest
from ..filter.perf import Perf

def run(target, mode, runTarget, compiler, profileMethod, valgrind):
    filterchain = FilterChain()
    if valgrind:
        filterchain.addFilter(ValgrindMemcheck())

    if profileMethod == 'perf':
        filterchain.addFilter(Perf(getBuildDir(mode, compiler)))

    if runTarget == 'unittest':
        filterchain.addFilter(RunUnittest(target, mode, compiler))
    elif runTarget == 'performance':
        filterchain.addFilter(RunPerformancetest(target, mode, compiler))
    else:
        print("Invalid run target: " + runTarget)
        return False
    if not filterchain.execute():
        return False

def runner(targets, mode, runTargets, compiler, profileMethod, valgrind):
    for target in targets:
        if target == 'all':
            for target in getAllRealTargets(getCurrentDir()):
                for runTarget in runTargets:
                    if runTarget == 'all':
                        run(target, mode, 'unittest', compiler, profileMethod, valgrind)
                        run(target, mode, 'performance', compiler, profileMethod, valgrind)
                    else:
                        run(target, mode, runTarget, compiler, profileMethod, valgrind)
        else:
            for runTarget in runTargets:
                if runTarget == 'all':
                    run(target, mode, 'unittest', compiler, profileMethod, valgrind)
                    run(target, mode, 'performance', compiler, profileMethod, valgrind)
                else:
                    run(target, mode, runTarget, compiler, profileMethod, valgrind)
