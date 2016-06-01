#!/usr/bin/python

import os
import subprocess

BUILD_DIR = 'build'
BIN_DIR = 'bin'
SRC_DIR = 'src'
EXIT_SUCCESS = 0

def listToString(list, separator):
    return separator.join(list)

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

def getBuildDirWithoutMode():
    return BUILD_DIR

def getBuildDir(mode, compiler):
    return BUILD_DIR + '/' + compiler + '/' + mode

def getBinDir(mode):
    return BIN_DIR + '/' + mode

def getUnittestDir(mode, compiler):
    return getBuildDir(mode, compiler) + '/bin/test/unittest'

def getPerformancetestDir(mode, compiler):
    return getBuildDir(mode, compiler) + '/bin/benchmark'

def getSrcDir(target = None):
    if target is None or target == 'all':
        return SRC_DIR
    return SRC_DIR + '/' + target

def executeInShell(cmd, working_directory = '.'):
    pwd()
    print("\nExecuting '{0}' in '{1}'".format(listToString(cmd, ' '), working_directory))
    retValue = subprocess.call(cmd, cwd = working_directory)
    return retValue

def getShellOutput(cmd, working_directory = '.'):
    print("\nExecuting '{0}' in '{1}'".format(listToString(cmd, ' '), working_directory))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd = working_directory)
    out, err = process.communicate()
    return out,err

def isInstalled(binary):
    cmd = ['which', binary]
    return isSuccess(executeInShell(cmd))

def getAllDirs(path):
    dirs = [x[0] for x in os.walk(path)]
    for root, dirs, files in os.walk(path):
        return dirs

def getAllFiles(path):
    dirs = [x[0] for x in os.walk(path)]
    for root, dirs, files in os.walk(path):
        return files

def isSuccess(retValue):
    return retValue == EXIT_SUCCESS
