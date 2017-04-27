import sys
from lib import config
#from lib import cheats
from lib import module
from lib import game

def show_module():
    x = module.file.read()
    return
def set_module_native():
    module.file.write(module.native() )
def set_module_viking():
    module.file.write(module.viking_conquest() )
def set_module_napoleonic():
    module.file.write(module.napoleonic_wars() )
