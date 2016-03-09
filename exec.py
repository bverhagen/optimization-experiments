#!/usr/bin/python

import argparse

from exec_utils.util.util import *
from exec_utils.cmd.cmd import *

def execute(commands, mode, targets):
    for command in commands:
        if(command == 'init'):
            init(getCurrentDir(), mode);
        elif(command == 'build'):
            for target in targets:
                build(target, mode)
        elif(command == 'clean'):
            for target in targets:
                clean(target, mode)
        elif(command == 'distclean'):
            distclean(mode)
        elif(command == 'rebuild'):
            execute(['clean', 'build'], mode, targets)
        else:
            print("Error: invalid command")


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
    parser.add_argument('-t', '--target', nargs='+', choices=targetOptions, default='all',
		   help="Target to build.")

    args = parser.parse_args()
    execute(args.commands, args.mode, args.target)
    pass

if __name__ == "__main__":
    main()
