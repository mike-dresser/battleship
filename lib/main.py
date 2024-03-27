# from game import Game
# from curses import wrapper

# def main(stdscr):
#     """ Main game loop. `stdscr` is curses screen object"""
#     play_again = True
#     while play_again:
#         '''Game returns False to exit'''

#         x = Game(stdscr)
#         play_again = x.play()

# # Run `wrapper` to initialize curses, pass main loop
# wrapper(main)

### Above code is working production - below is testing with colors
import curses
from game import Game
from curses import wrapper
from assets import logo_a

def main(stdscr):
    """Main game loop. `stdscr` is curses screen object"""
    
    # curses.curs_set(0)
    # stdscr.clear()

    # curses.start_color()
    # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)  # Define a pair with red text on black background

  
    # # logo_lines = logo_a()
    # stdscr.addstr(0, 0, logo_a(), curses.color_pair(1))  
    
  
    # stdscr.refresh()
    # stdscr.getch()

    play_again = True
    while play_again:
#         '''Game returns False to exit'''

        x = Game(stdscr)
        play_again = x.play()
    # Initialize curses

# Run `wrapper` to initialize curses, pass main loop
wrapper(main)