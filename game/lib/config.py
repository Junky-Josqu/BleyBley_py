import shutil
from os.path import expanduser
home = expanduser("~")

def call_backup():
    shutil.move('backup/own.py', 'configs/own.py')
def move():
    shutil.move('configs/own.py', '%s/.mbwarband/rgl_config.txt' % (home))
