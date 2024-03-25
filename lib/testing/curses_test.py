import curses
from curses import wrapper
import time

def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_RED)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)
    stdscr.addstr("Hello, world")
    stdscr.refresh()
    counter_win = curses.newwin(1, 20, 10, 10)

    for i in range(100):
        counter_win.clear()
        color = curses.color_pair(2)
        if i % 2 == 0:
            color = curses.color_pair(1)
        counter_win.addstr(f'Count: {i}', color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)
