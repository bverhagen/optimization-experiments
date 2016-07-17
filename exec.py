#!/usr/bin/python

import argparse

from exec_utils.util.util import *
from exec_utils.cmd.cmd import *
from exec_utils.options.options import Options
import sys

EXIT_SUCCESS = 0
EXIT_ERROR = 1

def execute(options):
    for command in options.getCommands():
        if(command == 'init'):
            if not init(options.getCurrentDir(), options):
                return False
        elif(command == 'build'):
            if not build(options):
                print("Build failed")
                return False
        elif(command == 'clean'):
            if not clean(options):
                print("Clean failed")
                return False
        elif(command == 'distclean'):
                if not distclean(options):
                    return False
        elif(command == 'run'):
            if not run(options):
                return False
        elif(command == 'analyze'):
            if not analyze(options):
                return False
        else:
            print("Error: invalid command")
            return False

    return True


def main():
    args = Options()        # Until Options.parse() is called, the getters will return the default values

    commandOptions = ['init', 'build', 'clean', 'distclean', 'rebuild', 'run', 'analyze']
    buildModeOptions = ['debug', 'release']
    targetOptions = getTargets(args.getCurrentDir())
    runTargetOptions = getRunTargets()
    compilerOptions = ['gcc', 'clang']
    analyzeOptions = getAnalyzeMethods()
    profileOptions = ['none', 'perf', 'callgrind']

    parser = argparse.ArgumentParser(description='Convenience script for executing commands')
    parser.add_argument('commands', metavar='commands', nargs='+', choices=commandOptions,
		   help="Commands to execute. Possible values: {0}.".format(commandOptions))
    parser.add_argument('-m', '--mode', choices=buildModeOptions, default=args.getModes(),
		   help="Build mode to use.")
    parser.add_argument('-t', '--target', nargs='+', choices=targetOptions, default=args.getTargets(),
		   help="Target to build.")
    parser.add_argument('-r', '--run', nargs='+', choices=runTargetOptions, default=args.getRunTargets(),
		   help="Modes of the target to run.")
    parser.add_argument('-c', '--compiler', nargs='+', choices=compilerOptions, default=args.getCompilers(),
		   help="Compiler to use.")
    parser.add_argument('-w', '--valgrind', action='store_true', help="Enable valgrind memcheck. Only applicable on the run command")
    parser.add_argument('-b', '--show-stuff', action='store_true', help="Enable this to automatically open or show the results")
    parser.add_argument('-v', '--verbose-make', action='store_true', help="Enable make in verbose mode")
    parser.add_argument('-s', '--build-single-threaded', action='store_true', help="Build in single threaded mode")
    parser.add_argument('-a', '--analyze-method', nargs='+', choices=analyzeOptions, default=args.getAnalyzeMethods(),
		   help="Run analysis.")
    parser.add_argument('-l', '--profile-method', nargs='+', choices=profileOptions, default=args.getProfileMethods(),
		   help="Select performance tool.")
    parser.add_argument('-p', '--toolchain-path', nargs=1, default=args.getToolchainPath(),
		   help="Path to the compiler")

    args.parse(parser.parse_args())
    print('Commands = {0}'.format(listToString(args.getCommands(), ' - ')))
    print('Build mode = {0}'.format(args.getModes()))
    print('Target = {0}'.format(listToString(args.getTargets(), ' - ')))

    retCode = execute(args)

    if retCode:
        sys.exit(EXIT_SUCCESS)
    else:
        sys.exit(EXIT_ERROR)

if __name__ == "__main__":
    main()
