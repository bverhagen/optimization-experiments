#!/usr/bin/python

from .cmake import Cmake

buildSystem = Cmake()

def initBuildSystem(workingDir, mode):
    return buildSystem.init(workingDir, mode)

def buildBuildSystem(target, mode, verbose):
    return buildSystem.build(target, mode, verbose)

def cleanBuildSystem(target, mode, verbose):
    return buildSystem.clean(target, mode, verbose)

def distcleanBuildSystem(mode):
    return buildSystem.distclean(mode)
