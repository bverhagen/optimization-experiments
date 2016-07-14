from .valgrind import *

class ValgrindMemcheck(Valgrind):
    def __init__(self):
       super(ValgrindMemcheck, self).__init__('memcheck')
