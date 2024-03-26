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
    
    def update(self, string=''):
        """Update curses window with header, queue contents, and parameter str passed in (all optional)"""
        self.w.clear()
        self.w.addstr(self.header)
        self.w.addstr(self.add_queue)
        self.w.addstr(string)
        self.w.refresh()
        self.add_queue = ''

    def add(self, string):
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