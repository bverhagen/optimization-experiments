#!/usr/bin/python

from .cmake import Cmake
from .b2 import B2

buildSystem = B2()

def initBuildSystem(workingDir, mode):
    return buildSystem.init(workingDir, mode)

def buildBuildSystem(target, mode, verbose):
    return buildSystem.build(target, mode, verbose)

def cleanBuildSystem(target, mode, verbose):
    return buildSystem.clean(target, mode, verbose)

def distcleanBuildSystem(mode):
    return buildSystem.distclean(mode)
