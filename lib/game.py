from grid import Grid
import os
import random
from time import sleep
import curses

class Game:
    """Class to represent the current game"""

    def __init__(self, stdscr):
        """Main class to control gameplay
        
        Parameter:
            stdscr (obj): the curses object representing the screen"""
        self.player_grid = Grid(stdscr) 
        self.cpu_grid = Grid(stdscr) 
        self.s = stdscr
        self.header = self.new_window(12, 60, 0, 0) 
        self.user_msg = self.new_window(5, 80, curses.LINES - 5, 1)
        self.player_win = self.new_window(15, 20, 12, 3)
        self.cpu_win = self.new_window(15, 20, 12, 25)
            
    def new_window(self, height, width, begin_y, begin_x):
        """Return new curses window
        
        Parameters:
            height (int): window height in text lines
            width (int):  window width in columns
            begin_y (int): y coordinate for top left corner
            begin_x (int): x coordingate for top left corner"""

        return curses.newwin(height, width, begin_y, begin_x)
          
    def play(self):
        """Begin new game"""
        play_again = True
        while play_again:
            '''for right now I have the while loop on the whole play() but I think we should figure out a more efficient way
            Enables the "P to play again" at the end of a game'''

            self.s.clear()
            self.header.clear()
            self.header.addstr(''' 
                (          (       ) (   (    (     
            (  )\ )  *   ))\ ) ( /( )\ ))\ ) )\ )  
            ( )\(()/(` )  /(()/( )\()|()/(()/((()/(  
            )((_)/(_))( )(_))(_)|(_)\ /(_))(_))/(_)) 
            ((_)_(_)) (_(_()|_))  _((_|_))(_)) (_))   
            | _ )_ _||_   _/ __|| || |_ _| _ \/ __|  
            | _ \| |   | | \__ \| __ || ||  _/\__ \  
            |___/___|  |_| |___/|_||_|___|_|  |___/
            _________________________________________
            ''')
            self.header.refresh()
        

            self.player_win.addstr("~~HARBOR~~\n")
            self.player_win.addstr(self.player_grid.display_game_board())
            self.player_win.refresh()

            self.place_ships()
            self.cpu_win.addstr("~~BATTLEFIELD~~\n")
            self.cpu_grid.cpu_ship_placement()
            self.cpu_win.addstr(self.cpu_grid.display_game_board())
            self.cpu_win.refresh()
            
            # '''battle_on() checking for any ship on either grid'''
            # while self.battle_on(self.player_grid) and self.battle_on(self.cpu_grid):
            #     self.take_player_shot()
            #     input("Press any key to continue...")

            #     if not self.battle_on(self.cpu_grid):
            #         print("Congratulations! You win!")
            #         break

            #     self.take_cpu_shot()
            #     input("Press any key to continue...")
            #     if not self.battle_on(self.player_grid):
            #         print("Sorry, you lose!")
            #         break
            
            # self.user_msg.addstr("Press 'P' to play again, or any other key to exit: ")
            # self.user_msg.refresh()
            # play_again_input = self.user_msg.getkey()
            # if play_again_input.lower() != 'p':
            #     play_again = False


    def place_ships(self):
        """Place player ships"""
        placed_ships = 0
        while placed_ships < 3:
            self.user_msg.clear()
            self.user_msg.addstr('Begin by placing your 1x1 ships on the game board.\n')
            self.user_msg.addstr(f'*** {3 - placed_ships} ships remaining ***\n')
            pos = self.get_position_input('Position for your ship (i.e. "B2") ')
            self.user_msg.refresh()
            if self.player_grid.query_position(pos[0], pos[1]) == 'S':
                self.user_msg.addstr('Cannot place a ship on top of another!\n')
                self.user_msg.refresh()
                continue
            self.player_grid.place_ship(pos[0], pos[1])
            placed_ships += 1
            self.player_win.clear()
            self.player_win.addstr(self.player_grid.display_game_board())
            self.player_win.refresh()
        self.ships_placed = True

    def get_position_input(self, message):
        """Ensure player input is a valid two-character string like 'A1', case-insensitive.
        
        Parameters:
            message (str): display message for input field

        Return:
            str (length 2)
        """
        accepted = False
        while not accepted:
            self.user_msg.addstr(message)
            self.user_msg.refresh()
            curses.echo()
            value = self.user_msg.getstr()
            return_char = ''
            for num in value:
                return_char += chr(num)
            value = return_char
            result = ''
            if not len(value) == 2:
                self.user_msg.addstr('Position must be two characters!')
                self.user_msg.refresh()
                continue
            if value[0].upper() in 'ABCDE':
                result += value[0].upper()
            else:
                self.user_msg.addstr('First value must be valid letter!')
                self.user_msg.refresh()
                                     
                continue
            if value[1].isnumeric() and int(value[1]) <= 5:
                result += value[1]
            else:
                self.user_msg.addstr('Second value must be a valid number!')
                self.user_msg.refresh()
                                     
                continue
            accepted = True
        return result

    
    ##-Outline for Player Fire
    
    def take_player_shot(self):
        os.system('clear')
        print("~~HARBOR~~")
        self.player_grid.display_game_board()
        # print("~~BATTLEFIELD~~")
        # self.cpu_grid.display_game_board()
        
        print('''
  _____ _   _  _____     _   ___ __  __ 
 |_   _/_\ | |/ | __|   /_\ |_ _|  \/  |
   | |/ _ \| ' <| _|   / _ \ | || |\/| |
   |_/_/ \_|_|\_|___| /_/ \_|___|_|  |_|
''')
        print("~~BATTLEFIELD~~")
        self.cpu_grid.display_game_board()

        pos = self.get_position_input('Enter position to fire : ')
        row = pos[0]
        column = pos[1]
        if self.cpu_grid.query_position(row, column) in ['H', 'M']:
            print('Already fired at this position. Try again!')
        
        else:
            result = self.cpu_grid.query_position(row, column)
            if result == 'S':
                os.system('clear')
                
                print('''
   __ ______________
  / // /  _/_  __/ /
 / _  // /  / / /_/ 
/_//_/___/ /_/ (_)
''')
                self.cpu_grid.change_grid(row, column, '💥')
            else:
                os.system('clear')
            
                print('''
   __  _________________
  /  |/  /  _/ __/ __/ /
 / /|_/ // /_\ \_\ \/_/ 
/_/  /_/___/___/___(_) 
                      ''')
                self.cpu_grid.change_grid(row, column, '💦')

    def take_cpu_shot(self):
            os.system('clear')
            print('''
  _________    __ __ ______   __________ _    ____________ 
 /_  __/   |  / //_// ____/  / ____/ __ | |  / / ____/ __ |
  / / / /| | / ,<  / __/    / /   / / / | | / / __/ / /_/ /
 / / / ___ |/ /| |/ /___   / /___/ /_/ /| |/ / /___/ _, _/ 
/_/ /_/  |_/_/ |_/_____/   \____/\____/ |___/_____/_/ |_| 
                   ''')
            sleep(1)
            

            """CPU shot - random position"""
            while True:
                row = random.choice(self.player_grid.row_labels)
                column = random.choice(self.player_grid.column_labels)
                if self.player_grid.query_position(row, column) in ['H', 'M']:
                    print("CPU already fired at this position. Trying again...")
                    continue
                else:
                    break
            
            result = self.player_grid.query_position(row, column)
            if result == 'S':
                
                print('''
   __ ______________
  / // /  _/_  __/ /
 / _  // /  / / /_/ 
/_//_/___/ /_/ (_)  
                      ''')
                self.player_grid.change_grid(row, column, '💥')
            else:
                
                print('''
   _______   __________
  / __/ _ | / __/ __/ /
 _\ \/ __ |/ _// _//_/ 
/___/_/ |_/_/ /___(_)
                      ''')
                self.player_grid.change_grid(row, column, '💦')
                            
    
    def battle_on(self, grid):
    #  """Check for ships on grid. If no ships on either grid, battle over"""
        for row in grid.state:
            if 'S' in row:
                return True
        return False

