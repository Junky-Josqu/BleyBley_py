import shutil

def call_backup():
    shutil.move('backup/own.py', 'configs/own.py')
def move():
    shutil.move('configs/own.py', '~/.mbwarband/rgl_config.txt')
