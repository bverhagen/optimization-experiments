from exec_utils.util.util import *

class Options:
    def __init__(self):
        self.commands = []
        self.modes = 'release'
        self.targets= ['all']
        self.runTargets= ['all']
        self.compilers = ['gcc']
        self.valgrindMemcheck = False       # TODO convert this to an analysis parameter
        self.showStuff = False
        self.verbosity = False
        self.buildSingleThreaded = False
        self.analyzeMethods = ['clang']
        self.profileMethods = ['none']
        self.toolchainPath = ['']
        pass 

    def parse(self, args):
        """ Parse the given arguments. Calling the respective getters before this function is called, results in the default values being returned. """
        self.commands = args.commands
        self.modes = args.mode
        self.targets = args.target
        self.runTargets = args.run
        self.compilers = args.compiler
        self.valgrindMemcheck = args.valgrind
        self.verbosity = args.verbose_make
        self.buildSingleThreaded = args.build_single_threaded
        self.analyzeMethods = args.analyze_method
        self.toolchainPath = args.toolchain_path[0]
        self.profileMethods = args.profile_method 
        self.showStuff = args.show_stuff

    @staticmethod
    def replaceWith(hayStack, needle, replacementNeedle):
        while hayStack.count(needle) > 0:
            index = hayStack.index(needle)
            hayStack.pop(index)
            insertIndex = index
            for replacement in replacementNeedle:
                hayStack.insert(insertIndex, replacement) 
                insertIndex = insertIndex + 1

    def getCommands(self):
        self.replaceWith(self.commands, 'rebuild', ['distclean', 'build'])
        return self.commands

    def getModes(self):
        return self.modes

    def getTargets(self):
        self.replaceWith(self.targets, 'all', getAllRealTargets(getCurrentDir())) 
        return self.targets

    def getRunTargets(self):
        return self.runTargets

    def getCompilers(self):
        return self.compilers

    def getValgrindMemcheck(self):
        return self.valgrindMemcheck

    def getVerbosity(self):
        return self.verbosity

    def buildSingleThreaded(self):
        return self.buildSingleThreaded

    def getAnalyzeMethods(self):
        return self.analyzeMethods

    def getToolchainPath(self):
        return self.toolchainPath

    def getProfileMethods(self):
        return self.profileMethods

    def showStuff(self):
        return self.showStuff