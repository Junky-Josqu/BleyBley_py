# -*- coding: iso-8859-1 -*-
#For different Modules

from os.path import expanduser
home = expanduser("~")
x = '%s/.mbwarband/last_module_warband' % (home)
file = open(x,'r+')


def native():
    module = 'Native'
    return module

def viking_conquest():
    module = 'Viking Conquest'
    return module

def napoleonic_wars():
    module = 'Napoleonic Wars'
    return module
