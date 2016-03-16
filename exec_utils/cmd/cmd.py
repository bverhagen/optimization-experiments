#!/usr/bin/python

from ..util.util import executeInShell
from ..vcsSystem.vcsSystem import *
from ..buildSystem.buildSystem import *

def init(workingDir, mode):
    return initVcs() and initBuildSystem(workingDir, mode)

def build(target, mode):
    return buildBuildSystem(target, mode)

def clean(target, mode):
    return cleanBuildSystem(target, mode)

def distclean(mode):
    return distcleanBuildSystem(mode)
    # TODO: Use python to clean python files
