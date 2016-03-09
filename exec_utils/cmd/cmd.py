#!/usr/bin/python

from ..util.util import executeInShell
from ..vcsSystem.vcsSystem import *
from ..buildSystem.buildSystem import *

def init(workingDir, mode):
    initVcs()
    initBuildSystem(workingDir, mode)

def build(target, mode):
    buildBuildSystem(target, mode)

def clean(target, mode):
    cleanBuildSystem(target, mode)

def distclean(mode):
    distcleanBuildSystem(mode)

    # Use python to clean python files
