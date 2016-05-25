from compilerEnumerations import *
import gcc

class Clang(gcc.Gcc):
    def __init__(self, env, toolchain):
        self.setupToolChain(env, toolchain)

    @staticmethod
    def setupToolChain(env, toolchain):
        env['CXX'] = toolchain + 'clang++'

    @staticmethod
    def stopAtAssembler(env):
        env['CPPFLAGS'].extend(['-S', '-fverbose-asm'])
