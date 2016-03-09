#!/usr/bin/python

from ..util.util import executeInShell

class Git:
    def __init__(self):
        pass

    def init(self):
        executeInShell(["git","submodule", "init"])
        executeInShell(["git","submodule", "update"])
