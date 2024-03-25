from game import Game
from curses import wrapper

def main(stdscr):
    """ Main game loop. `stdscr` is curses screen object"""
    x = Game(stdscr)
    x.play()

# Run `wrapper` to initialize curses, pass main loop
wrapper(main)