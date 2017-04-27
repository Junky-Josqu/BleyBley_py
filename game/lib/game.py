import os
def start():
    game_loc = 'steam://rungameid/48700'
    os.system('steam %s') % (game_loc)
