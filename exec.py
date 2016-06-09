#!/usr/bin/python

import argparse

from exec_utils.util.util import *
from exec_utils.cmd.cmd import *
import sys

EXIT_SUCCESS = 0
EXIT_ERROR = 1

def execute(commands, mode, targets, runTargets, compilers, valgrind, verbose, singleThreaded, analyzeMethods):
    for command in commands:
        if(command == 'init'):
            if not init(getCurrentDir(), mode):
                return EXIT_ERROR
        elif(command == 'build'):
            for target in targets:
                for runMode in runTargets:
                    for compiler in compilers:
                        if not build(target, mode, runMode, compiler, verbose, singleThreaded):
                            return EXIT_ERROR
        elif(command == 'clean'):
            for target in targets:
                for compiler in compilers:
                    if not clean(target, mode, compiler, verbose):
                        return EXIT_ERROR
        elif(command == 'distclean'):
            for compiler in compilers:
                if not distclean(mode, compiler):
                    return EXIT_ERROR
        elif(command == 'rebuild'):
            if not execute(['clean', 'build'], mode, targets, compilers, valgrind, verbose, singleThreaded):
                return EXIT_ERROR
        elif(command == 'run'):
            for compiler in compilers:
                if not run(targets, mode, runTargets, compiler, valgrind):
                    return EXIT_ERROR
        elif(command == 'analyze'):
            for analyzeMethod in analyzeMethods:
                for target in targets:
                    if not analyze(analyzeMethod, mode, target, verbose):
                        return EXIT_ERROR
        else:
            print("Error: invalid command")
            return EXIT_ERROR

    return EXIT_SUCCESS


def main():
    commandOptions = ['init', 'build', 'clean', 'distclean', 'rebuild', 'run', 'analyze']
    buildModeOptions = ['debug', 'release']
    targetOptions = getAllDirs('{rootDir}/src'.format(rootDir=getCurrentDir()))
    targetOptions.extend(['all', 'unittest', 'performance'])
    runTargetOptions = ['unittest', 'performance', 'all']
    compilerOptions = ['gcc', 'clang']
    analyzeOptions = ['clang', 'cppcheck', 'cpplint']

    parser = argparse.ArgumentParser(description='Convenience script for executing commands')
    parser.add_argument('commands', metavar='commands', nargs='+', choices=commandOptions,
		   help="Commands to execute. Possible values: {0}.".format(commandOptions))
    parser.add_argument('-m', '--mode', choices=buildModeOptions, default='release',
		   help="Build mode to use.")
    parser.add_argument('-t', '--target', nargs='+', choices=targetOptions, default=['all'],
		   help="Target to build.")
    parser.add_argument('-r', '--run', nargs='+', choices=runTargetOptions, default=['all'],
		   help="Modes of the target to run.")
    parser.add_argument('-c', '--compiler', nargs='+', choices=compilerOptions, default=['gcc'],
		   help="Compiler to use.")
    parser.add_argument('-w', '--valgrind', action='store_true', help="Enable valgrind memcheck. Only applicable on the run command")
    parser.add_argument('-v', '--verbose-make', action='store_true', help="Enable make in verbose mode")
    parser.add_argument('-s', '--build-single-threaded', action='store_true', help="Build in single threaded mode")
    parser.add_argument('-a', '--analyze-method', nargs='+', choices=analyzeOptions, default=['clang'],
		   help="Run analysis.")

    args = parser.parse_args()
    print('Commands = {0}'.format(listToString(args.commands, ' - ')))
    print('Build mode = {0}'.format(args.mode))
    print('Target = {0}'.format(listToString(args.target, ' - ')))

    sys.exit(execute(args.commands, args.mode, args.target, args.run, args.compiler, args.valgrind, args.verbose_make, args.build_single_threaded, args.analyze_method))

if __name__ == "__main__":
    main()
