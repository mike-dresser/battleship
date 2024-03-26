import curses
from curses import wrapper
import time

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

def main(stdscr):
    curses.curs_set(0)  
    stdscr.clear()
    stdscr.addstr(0, 0, under_fire_a())
    stdscr.refresh()

    progress = 0.0
    while progress <= 1.0:
        incoming(stdscr, progress)
        progress += 0.1
        time.sleep(0.5)  

def under_fire_a():
    return '''
                _  _ _  _ ___  ____ ____        
                |  | |\ | |  \ |___ |__/        
                |__| | \| |__/ |___ |  \                        
                    ____  _ ____ ____      
                    |___  | |__/ |___      
                    |     | |  \ |___     
        ________________________________________
                            
'''

curses.wrapper(main)
