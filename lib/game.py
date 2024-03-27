from grid import Grid
from window import Window
import random
from time import sleep
import curses
from assets import *

class Game:
    """Class to represent the current game"""


    def __init__(self, stdscr):
        """Main class controlling gameplay
        
        Parameter:
            stdscr (obj): the curses object representing the screen; curses wrapper() passes this object, but I have not used it yet; the curses window objects handle all screen updates"""
        self.player_grid = Grid() 
        self.cpu_grid = Grid() 
        self.header = Window(11, 60, 0, 0) 
        # self.header.border()
        self.user_msg = Window(6, 40, 21, 6)
        self.player_win = Window(10, 19, 11, 5, "    ~~HARBOR~~\n")
        self.cpu_win = Window(10, 19, 11, 35, "  ~~BATTLEFIELD~~\n")
        self.player_shot = 0# self.ship_length = 1
    
    def draw_quit_message(self):
        """Draws the quit message on the screen"""
        self.stdscr.addstr(curses.LINES - 3, 0, "Press 'Q' to quit")

    def play(self):
        """Begin new game
        
        Return True to play again, False to exit."""
        # curses.start_color()
        # curses.curs_set(0)
        # curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK) 

        self.header.update(logo_a(), 6)
        self.player_win.update(self.player_grid.display_game_board())
        self.cpu_win.update(self.cpu_grid.display_game_board())

        self.place_ships()
        self.cpu_grid.toggle_ship_visibility() # hide CPU ship positions by default
        self.cpu_grid.cpu_ship_placement()
        self.cpu_win.update(self.cpu_grid.display_game_board())
        
        '''battle_on() checking for any ship on either grid'''
        while self.battle_on(self.player_grid) and self.battle_on(self.cpu_grid):
            self.take_player_shot()

            if not self.battle_on(self.cpu_grid):
                self.header.update(victory_a(),5)
                self.user_msg.add(f"Congratulations! You won in {self.player_shot} shots!\n\n")

                break

            self.take_cpu_shot()
            if not self.battle_on(self.player_grid):
                self.user_msg.add("Sorry, you lose!")
                break
        
    
        self.user_msg.update("Press 'P' to play again, or any other key to exit: ")
        play_again_input = self.user_msg.get_input()
        if play_again_input.lower() != 'p':
           return False 
        return True

    def place_ships(self):
        """Place player ships"""
        placed_ships = 0
        while placed_ships < 3:
            self.user_msg.add('Begin by placing your ships in the harbor.\n')
            self.user_msg.add(f'*** {3 - placed_ships} ships remaining ***\n')
            pos = self.get_position_input('Position for your ship (i.e. "B2") ')
            if Grid.SHIP_SIZE > 1:
                 horizontal = self.get_orientation(f'Position: {pos}\nOrientation: [H]orizontal or [V]ertical? ')
            else:
                horizontal = True
            if not self.player_grid.valid_ship_placement(pos, horizontal, Grid.SHIP_SIZE):
                curses.curs_set(0) #hide cursor while drawing headers
                self.user_msg.update('The ship cannot fit here!\nPress any key to try again...')
                self.player_win.get_input()
                continue
            self.player_grid.place_ship(pos, horizontal)
            placed_ships += 1
            self.player_win.update(self.player_grid.display_game_board())
        self.ships_placed = True
    
    def get_orientation(self, message):
        """Get ship orientation (horizontal or vertical)
        
        Return:
            boolean: True == horizontal"""
        accepted = False
        while not accepted:
            self.user_msg.update(message)
            curses.echo()
            value = self.user_msg.get_input()
            try:
                if not value[0].lower() in ['v', 'h']:
                    self.user_msg.add('Please choose V or H!\n')
                    continue
            except:
                self.user_msg.add('Please enter V or H...\n')
                continue
            if value[0].lower() == 'v':
                return False
            if value[0].lower() == 'h':
                return True
                
    def get_position_input(self, message):
        """Ensure player input is a valid two-character string like 'A1', case-insensitive.
        
        Parameters:
            message (str): display message for input field, a la python input()

        Return:
            str (length == 2)
        """
        accepted = False
        while not accepted:
            self.user_msg.update(message)
            curses.echo()
            value = self.user_msg.get_input()
            result = ''
            try:
                if value.upper() == 'XX':
                    self.cpu_grid.toggle_ship_visibility()
                    self.cpu_win.update(self.cpu_grid.display_game_board())
            except:        
                pass
            if not len(value) == 2:
                self.user_msg.update('Position must be two characters!')
                continue
            if value[0].upper() in 'ABCDE':
                result += value[0].upper()
            else:
                self.user_msg.update('First value must be valid letter!\n')
                continue
            if value[1].isnumeric() and int(value[1]) <= 5:
                result += value[1]
            else:
                self.user_msg.update('Second value must be a valid number!\n')
                                     
                continue
            accepted = True
        return result

    
    ##-Outline for Player Fire
    
    def take_player_shot(self):
        curses.curs_set(0) #hide cursor while drawing headers
        self.player_win.add(self.player_grid.display_game_board())
        self.player_win.update(f'  {len(self.player_grid.ships)} ships afloat\n')
        self.header.update(take_aim_a(),5)
        self.cpu_win.add(self.cpu_grid.display_game_board())
        self.cpu_win.update(f'  {len(self.cpu_grid.ships)} ships afloat\n')
        curses.curs_set(1)
        pos = self.get_position_input('Enter position to fire : ')
        row = pos[0]
        column = pos[1]
        curses.curs_set(0) #hide cursor while drawing headers
        if self.cpu_grid.query_position(row, column) in ['H', 'M']:
            self.user_msg.add('Already fired at this position. Try again!')
        
        ### the following code is repeteded in take_cpu_shot, we can probably refactor this ###
        else:
            result = self.cpu_grid.fire_on(row, column)
            self.player_shot += 1
            outgoing(self.header)
            self.cpu_win.update(self.cpu_grid.display_game_board())
            if result == 'S':    
                self.header.update(hit_a(),1)
            else:
                self.header.update(miss_a(),2)
            sleep(2)

    def take_cpu_shot(self):
            self.header.update(take_cover_a(),5)
            sleep(2)
            curses.curs_set(0) #hide cursor while drawing headers
            incoming(self.header)
            sleep(2)

            
            """CPU shot - random position"""
            while True:
                row = random.choice(self.player_grid.row_labels)
                column = random.choice(self.player_grid.column_labels)
                if self.player_grid.query_position(row, column) in ['H', 'M']:
                    self.user_msg.update("CPU already fired at this position. Trying again...") # this message never shows, or only briefly. Add delay, or remove?
                    continue
                else:
                    break
            
            result = self.player_grid.fire_on(row, column)
            self.player_win.update(self.player_grid.display_game_board())

            if result == 'S':
                self.header.update(hit_a(),1)
                sleep(2)
            else:
                self.header.update(safe_a(),5)
            sleep(2)
    
    def battle_on(self, grid):
    #  """Check for ships on grid. If no ships on either grid, battle over"""
        for row in grid.state:
            if 'S' in row:
                return True
        return False
