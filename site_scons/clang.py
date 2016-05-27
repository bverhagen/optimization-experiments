from compilerEnumerations import *
import gcc

class Clang(gcc.Gcc):
    def __init__(self, env, toolchain):
        self.setupToolChain(env, toolchain)

    @staticmethod
    def setupToolChain(env, toolchain):
        env['CXX'] = toolchain + 'clang++'

        env['CPPPATH'] = []
        env['CPPFLAGS'] = []
        env['CXXFLAGS'] = []
        env['LDFLAGS'] = []
        env['CFLAGS'] = []
        env['LINKFLAGS'] = []


    @staticmethod
    def stopAtAssembler(env):
        env['CPPFLAGS'].extend(['-S', '-fverbose-asm'])
