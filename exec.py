#!/usr/bin/python

import argparse

from exec_utils.util.util import *
from exec_utils.cmd.cmd import *
import sys

EXIT_SUCCESS = 0
EXIT_ERROR = 1

def execute(commands, mode, targets):
    for command in commands:
        if(command == 'init'):
            if not init(getCurrentDir(), mode):
		return EXIT_ERROR
        elif(command == 'build'):
            for target in targets:
                if not build(target, mode):
			return EXIT_ERROR
        elif(command == 'clean'):
            for target in targets:
                if not clean(target, mode):
			return EXIT_ERROR
        elif(command == 'distclean'):
            if not distclean(mode):
		return EXIT_ERROR
        elif(command == 'rebuild'):
            if not execute(['clean', 'build'], mode, targets):
		return EXIT_ERROR
        else:
            print("Error: invalid command")
            return EXIT_ERROR

    return EXIT_SUCCESS


def main():
    commandOptions = ['init', 'build', 'clean', 'distclean', 'rebuild']
    buildModeOptions = ['debug', 'release']
    targetOptions = getAllDirs(getCurrentDir())
    targetOptions.append('all')

    parser = argparse.ArgumentParser(description='Convenience script for executing commands')
    parser.add_argument('commands', metavar='commands', nargs='+', choices=commandOptions,
		   help="Commands to execute. Possible values: {0}.".format(commandOptions))
    parser.add_argument('-m', '--mode', choices=buildModeOptions, default='release',
		   help="Build mode to use.")
    parser.add_argument('-t', '--target', nargs='+', choices=targetOptions, default=['all'],
		   help="Target to build.")

    args = parser.parse_args()
    sys.exit(execute(args.commands, args.mode, args.target))

if __name__ == "__main__":
    main()
