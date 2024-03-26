import curses
from curses import wrapper
import time
from assets import *

# def main(stdscr):
#     curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
#     curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
#     stdscr.addstr("Hello, world")
#     stdscr.refresh()
#     counter_win = curses.newwin(1, 20, 10, 10)

#     for i in range(10):
#         counter_win.clear()
#         color = curses.color_pair(2)
#         if i % 2 == 0:
#             color = curses.color_pair(1)
#         counter_win.addstr(f'Count: {i}', color)
#         counter_win.refresh()
#         time.sleep(0.1)
#     stdscr.getch()

# wrapper(main)



def incoming(stdscr, progress):
    stdscr.clear()
    stdscr.addstr(0, 0, under_fire_a())
    bar_width = 40
    fill_width = int(bar_width * progress)
    bar = '🛳️' + ' ' * (bar_width - fill_width - 1) + '💣' + '0' * fill_width + ']'
    stdscr.addstr(10, 10, bar)
    stdscr.addstr(0, 10, bar)
    stdscr.refresh()
  
def outgoing(stdscr, progress):
    stdscr.clear()
    stdscr.addstr(0, 0, bombs_away_a())
    bar_width = 40
    fill_width = int(bar_width * progress)
    empty_width = bar_width - fill_width - 1
    bar = '🛳️' + '0' * empty_width + '💣' + ' ' * fill_width + '🛳️'
    stdscr.addstr(10, 10, bar)
    stdscr.addstr(0, 10, bar)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  
    stdscr.clear()
    stdscr.addstr(0, 0, bombs_away_a() )
    stdscr.refresh()



    progress = 0.0
    while progress <= 1.0:
        incoming(stdscr, progress)
        progress += 0.1
        time.sleep(0.5)  
    
    progress = 1.0
    while progress >= 0.0:
        outgoing(stdscr, progress)
        time.sleep(0.5)
        progress -= 0.1

# def under_fire_a():
#     return '''
#                 _  _ _  _ ___  ____ ____        
#                 |  | |\ | |  \ |___ |__/        
#                 |__| | \| |__/ |___ |  \                        
#                     ____  _ ____ ____      
#                     |___  | |__/ |___      
#                     |     | |  \ |___     
#         ________________________________________
                            
# '''

# def bombs_away_a():
#         return '''
#                         ___  ____  __  ______  ____
#                        / _ )/ __ \/  |/  / _ )/ __/
#                       / _  / /_/ / /|_/ / _  |\ \  
#                      /____/\____/_/__/_/____/___/__
#                         / _ | | /| / / _ \ \/ /  / /
#                        / __ | |/ |/ / __ |\  /  /_/ 
#                       /_/ |_|__/|__/_/ |_|/_/  (_)  
#                 ________________________________________
#                              '''


curses.wrapper(main)
