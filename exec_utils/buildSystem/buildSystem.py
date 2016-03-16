#!/usr/bin/python

from .cmake import Cmake

buildSystem = Cmake()

def initBuildSystem(workingDir, mode):
    return buildSystem.init(workingDir, mode)

def buildBuildSystem(target, mode):
    return buildSystem.build(target, mode)

def cleanBuildSystem(target, mode):
    return buildSystem.clean(target, mode)

def distcleanBuildSystem(mode):
    return buildSystem.distclean(mode)
