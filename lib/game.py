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
        self.user_msg = Window(5, 80, curses.LINES - 5, 1)
        self.player_win = Window(15, 20, 11, 3, "    ~~HARBOR~~\n")
        self.cpu_win = Window(15, 20, 11, 35, "  ~~BATTLEFIELD~~\n")
        self.ship_length = 2
    
    def draw_quit_message(self):
        """Draws the quit message on the screen"""
        self.stdscr.addstr(curses.LINES - 3, 0, "Press 'Q' to quit")

    def play(self):
        """Begin new game
        
        Return True to play again, False to exit."""
        self.header.update(logo_a())
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
                self.user_msg.add("Congratulations! You win!\n\n")

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
            self.user_msg.add('Begin by placing your 1x2 ships in the harbor.\n')
            self.user_msg.add(f'*** {3 - placed_ships} ships remaining ***\n')
            pos = self.get_position_input('Position for your ship (i.e. "B2") ')
            if not self.player_grid.valid_ship_placement(pos, self.ship_length):
                curses.curs_set(0) #hide cursor while drawing headers
                self.user_msg.update('The ship cannot fit here!\nPress any key to try again...')
                self.player_win.get_input()
                continue
            self.player_grid.place_ship(pos)
            placed_ships += 1
            self.player_win.update(self.player_grid.display_game_board())
        self.ships_placed = True
    
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
        self.player_win.update(self.player_grid.display_game_board())
        self.player_win.add(f'{len(self.player_grid.ships)} ships afloat\n')
        self.header.update(take_aim_a())
        self.cpu_win.update(self.cpu_grid.display_game_board())
        self.cpu_win.add(f'{len(self.cpu_grid.ships)} ships afloat\n')
        curses.curs_set(1)
        pos = self.get_position_input('Enter position to fire : ')
        row = pos[0]
        column = pos[1]
        curses.curs_set(0) #hide cursor while drawing headers
        if self.cpu_grid.query_position(row, column) in ['H', 'M']:
            self.user_msg.add('Already fired at this position. Try again!')
        
        ### the following code is repeteded in take_cpu_shot, we can probably refactor this ###
        else:
            result = self.cpu_grid.query_position(row, column)
            if result == 'S':    
                self.cpu_grid.change_grid(row, column, '💥')
                self.cpu_win.update(self.cpu_grid.display_game_board())
                self.header.update(hit_a())
            else:
                self.cpu_grid.change_grid(row, column, '💦')
                self.cpu_win.update(self.cpu_grid.display_game_board())
                self.header.update(miss_a())
            sleep(1)

    def take_cpu_shot(self):
            curses.curs_set(0) #hide cursor while drawing headers
            self.header.update(under_fire_a())
            sleep(1)
            self.header.update(take_cover_a())
            sleep(1)
            
            """CPU shot - random position"""
            while True:
                row = random.choice(self.player_grid.row_labels)
                column = random.choice(self.player_grid.column_labels)
                if self.player_grid.query_position(row, column) in ['H', 'M']:
                    self.user_msg.update("CPU already fired at this position. Trying again...") # this message never shows, or only briefly. Add delay, or remove?
                    continue
                else:
                    break
            
            result = self.player_grid.query_position(row, column)
            if result == 'S':
                self.player_grid.change_grid(row, column, '💥')
                self.player_win.update(self.player_grid.display_game_board())
                self.header.update(hit_a())
            else:
                self.player_grid.change_grid(row, column, '💦')
                self.player_win.update(self.player_grid.display_game_board())
                self.header.update(safe_a())
            sleep(1)
    
    def battle_on(self, grid):
    #  """Check for ships on grid. If no ships on either grid, battle over"""
        for row in grid.state:
            if 'S' in row:
                return True
        return False
