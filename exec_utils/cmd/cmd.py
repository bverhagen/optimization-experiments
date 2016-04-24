#!/usr/bin/python

from ..util.util import executeInShell
from ..vcsSystem.vcsSystem import *
from ..buildSystem.buildSystem import *
from ..runner.runner import *

def init(workingDir, mode):
    return initVcs() and initBuildSystem(workingDir, mode)

def build(target, mode, verbose):
    return buildBuildSystem(target, mode, verbose)

def clean(target, mode, verbose):
    return cleanBuildSystem(target, mode, verbose)

def distclean(mode):
    return distcleanBuildSystem(mode)
    # TODO: Use python to clean python files

def run(target, mode, runTargets, valgrind):
    return runner(target, mode, runTargets, valgrind)
