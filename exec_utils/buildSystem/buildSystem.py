#!/usr/bin/python

from .cmake import Cmake

buildSystem = Cmake()

def initBuildSystem(workingDir, mode):
    buildSystem.init(workingDir, mode)

def buildBuildSystem(target, mode):
    buildSystem.build(target, mode)

def cleanBuildSystem(target, mode):
    buildSystem.clean(target, mode)

def distcleanBuildSystem(mode):
    buildSystem.distclean(mode)
