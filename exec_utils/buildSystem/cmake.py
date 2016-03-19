#!/usr/bin/python

import shutil

from ..util.util import *

class Cmake:
    def __init__(self):
        pass

    def init(self, workingDir, mode):
        buildPath = getBuildDir(mode)
        print("Initializing '{0}' build directory".format(buildPath))
        createDirIfNotExists(buildPath)

        modeFlag = "-DCMAKE_BUILD_TYPE=" + mode
        goToDir(buildPath)
        retValue = executeInShell(["cmake", modeFlag, "../.."])
        goToDir(workingDir)
        return isSuccess(retValue)

    def build(self, target, mode):
        buildDir = getBuildDir(mode)
        if(not target or target == 'all'):
            print("Building all targets in {0} mode".format(mode))
        else:
            print("Building target {0} in {1} mode".format(target, mode))
            buildDir = getBuildDir(mode) + '/' + target
        return isSuccess(executeInShell(["make", "-j", "-C", buildDir])) and isSuccess(executeInShell(["make", "install", "-C", buildDir]))

    def clean(self, target, mode):
        buildDir = getBuildDir(mode)
        if(target and target != 'all'):
            buildDir = getBuildDir(mode) + '/' + target

        print("Cleaning {0}".format(buildDir))
        return isSuccess(executeInShell(["make", "-C", buildDir, "clean" ]))

    def distclean(self, mode):
        buildDir = getBuildDir(mode)
        print("Dist cleaning {0}".format(buildDir))
        if exists(buildDir):
            shutil.rmtree(buildDir)
        return True
