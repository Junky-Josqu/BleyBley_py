import sys
from lib import conf
from lib import game
from lib import module
from lib import config

def show_module():
    x = module.file.read()
    return
def set_module_native():
    module.file.write(module.native() )
def set_module_viking():
    module.file.write(module.viking_conquest() )
def set_module_napoleonic():
    module.file.write(module.napoleonic_wars() )
