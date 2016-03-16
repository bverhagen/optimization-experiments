#!/usr/bin/python

import os
import subprocess

BUILD_DIR = 'build'
EXIT_SUCCESS = 0

def getCurrentDir():
    return os.getcwd()

def exists(path):
    return os.path.exists(path)

def createDirIfNotExists(path):
    if not exists(path):
        os.makedirs(path)

def goToDir(path):
    os.chdir(path)

def pwd():
    print("Current working dir: {0}".format(getCurrentDir()))

def getBuildDir(mode):
    return BUILD_DIR + '/' + mode

def executeInShell(cmd):
    pwd()
    print("Executing '{0}'".format(cmd))
    retValue = subprocess.call(cmd)
    print("Ret value = {0}".format(retValue))
    return retValue

def getAllDirs(path):
    dirs = [x[0] for x in os.walk(path)]
    for root, dirs, files in os.walk(path):
        return dirs

def isSuccess(retValue):
    return retValue == EXIT_SUCCESS
