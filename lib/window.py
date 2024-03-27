import curses

class Window:

    def __init__(self, height, width, begin_y, begin_x, header=''):
        """Represent curses windows and their methods
    
        Parameters:
            height (int): window height in rows (default terminal is ~25)
            width (int):   window width in columns (default terminal is ~80)
            begin_y (int): row position of top-left corner
            begin_x (int): column position for top-left corner
            header (str):  text string which will always be displayed at top of window
            """       
        self.height = height
        self.width = width
        self.begin_y = begin_y
        self.begin_x = begin_x
        self.w = curses.newwin(height, width, begin_y, begin_x)
        self.header = header
        self.add_queue = '' # queue to add when updating
        self.w.box() 
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_RED)
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_GREEN, curses.COLOR_BLACK)


    def update(self, string='',color_pair = 0):
        """Update curses window with header, queue contents, and parameter str passed in (all optional)"""
        self.w.clear()
        curses.start_color()
        curses.curs_set(0)
        # self.w.box() 
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        self.w.addstr(self.header, curses.color_pair(color_pair))
        self.w.addstr(self.add_queue, curses.color_pair(color_pair))
        self.w.addstr(string, curses.color_pair(color_pair))
        self.w.refresh()
        self.add_queue = ''
        

    def add(self, string,):
        """Add string to queue, but don't update."""
        self.add_queue += string

    def get_input(self):
        """Get user input and return as string
        
        curses .getstr() method returns a string of ASCII codes (a 'byte-object') which need to be converted"""
        value = self.w.getstr()
        return_char = ''
        for num in value:
            return_char += chr(num)
        return return_char