import glob
from ..util.util import *

def runCppcheck(target, verbose):
    binary_name = 'cppcheck'
    if not isInstalled(binary_name):
        print('Please install cppcheck or add it to your path.')

    includes = getAllDirsThatContainPattern(getSrcDir(), '.h')

    targetDir = getSrcDir(target)

    cmd = [binary_name]
    cmd.append('--enable=all')
    cmd.append('--std=c++11')
    cmd.append('--includes-file=cppcheck/includes.cppcheck')
    cmd.append('--config-excludes-file=cppcheck/excludes.cppcheck')
    cmd.append('--suppressions-list=cppcheck/suppressions.cppcheck')
    cmd.append('--force')
    cmd.append('--error-exitcode=1')
    if verbose:
        cmd.append('--verbose')
    else:
        cmd.append('-q')

    for include in includes:
        cmd.append('--include=' + include)

    cmd.append(targetDir)
#    cmd.append('--check-config')
    return isSuccess(executeInShell(cmd))
