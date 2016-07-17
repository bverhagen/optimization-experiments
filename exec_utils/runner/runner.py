#!/usr/bin/python

from ..util.util import *
from ..filter.filterchain import FilterChain
from ..filter.valgrindMemcheck import ValgrindMemcheck
from ..filter.valgrindCallgrind import ValgrindCallgrind
from ..filter.runUnitTest import RunUnittest
from ..filter.runPerformanceTest import RunPerformancetest
from ..filter.perf import Perf

def run(target, mode, runTarget, compiler, profileMethod, valgrind, showStuff):
    filterchain = FilterChain()
    if valgrind:
        filterchain.addFilter(ValgrindMemcheck())

    if profileMethod == 'perf':
        filterchain.addFilter(Perf(getBuildDir(mode, compiler), showStuff))

    if profileMethod == 'callgrind':
        filterchain.addFilter(ValgrindCallgrind(getBuildDir(mode, compiler), showStuff))

    if runTarget == 'unittest':
        filterchain.addFilter(RunUnittest(target, mode, compiler))
    elif runTarget == 'performance':
        filterchain.addFilter(RunPerformancetest(target, mode, compiler))
    else:
        print("Invalid run target: " + runTarget)
        return False
    return filterchain.execute()

def runner(target, mode, runTarget, compiler, profileMethod, valgrind, showStuff):
    return run(target, mode, runTarget, compiler, profileMethod, valgrind, showStuff)
