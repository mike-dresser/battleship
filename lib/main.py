import curses
from game import Game
from curses import wrapper

def main(stdscr):
    """Main game loop. `stdscr` is curses screen object"""
    

    play_again = True
    while play_again:
#         '''Game returns False to exit'''

        x = Game(stdscr)
        play_again = x.play()

wrapper(main)