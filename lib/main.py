from game import Game
from curses import wrapper

def main(stdscr):
    """ Main game loop. `stdscr` is curses screen object"""
    play_again = True
    while play_again:
        '''for right now I have the while loop on the whole play() but I think we should figure out a more efficient way
        Enables the "P to play again" at the end of a game'''

        x = Game(stdscr)
        play_again = x.play()

# Run `wrapper` to initialize curses, pass main loop
wrapper(main)