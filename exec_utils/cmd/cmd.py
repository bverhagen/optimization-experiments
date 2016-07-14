#!/usr/bin/python

from ..util.util import executeInShell
from ..vcsSystem.vcsSystem import *
from ..buildSystem.buildSystem import *
from ..runner.runner import *
from ..analyze.analyze import *

def init(workingDir, mode):
    return initVcs() and initBuildSystem(workingDir, mode)

def build(target, mode, runMode, compiler, toolchainPath, verbose, singleThreaded):
    return buildBuildSystem(target, mode, runMode, compiler, toolchainPath, verbose, singleThreaded)

def clean(target, mode, compiler, verbose):
    return cleanBuildSystem(target, mode, compiler, verbose)

def distclean(mode, compiler):
    return distcleanBuildSystem(mode, compiler)
    # TODO: Use python to clean python files

def run(target, mode, runTargets, compiler, profileMethod, valgrind, showStuff):
    return runner(target, mode, runTargets, compiler, profileMethod, valgrind, showStuff)

def analyze(method, mode, targets, verbose):
    return analyzeBuildSystem(method, mode, targets, verbose)
