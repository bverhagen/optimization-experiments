from ..util.util import *
from .filter import *

class Perf(Filter):
    def __init__(self, buildDir):
        self.outputFile = buildDir + '/../perf.data'

    def process(self, cmd):
        return cmd + ['perf', 'record', '-o', self.outputFile]

    def postProcess(self):
        cmd = ['perf', 'report', '-i', self.outputFile] 
        executeInShell(cmd)
