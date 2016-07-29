#!/usr/bin/python

from ..util.util import *
from ..filter.filterchain import FilterChain
from ..filter.runUnitTest import RunUnittest
from ..filter.runPerformanceTest import RunPerformancetest

def run(target, mode, runTarget, compiler, showStuff, filterchain = None):
    if filterchain is None:
        filterchain = FilterChain()

    if runTarget == 'unittest':
        filterchain.addFilter(RunUnittest(target, mode, compiler))
    elif runTarget == 'performance':
        filterchain.addFilter(RunPerformancetest(target, mode, compiler))
    else:
        print("Invalid run target: " + runTarget)
        return False
    return filterchain.execute()

def runner(target, mode, runTarget, compiler, showStuff, filterchain = None):
    return run(target, mode, runTarget, compiler, showStuff, filterchain)
