from grid import Grid
import os

class Game:
    """Class to represent the current game"""

    def __init__(self):
        self.player_grid = Grid() 
        self.cpu_grid = Grid() 
        # eventually we will have a computer grid as well
    
    def play(self):
        """Begin new game"""

        os.system('clear')
        print('~ ~ ~  B A T T L E S H I P  ~ ~ ~\n\n')
        print('The year is 2024. Oceans are battlefields.\n')
    
        print("~~HARBOR~~")
        self.player_grid.display_game_board()
        self.place_ships()
        print("~~BATTLEFIELD~~")
        self.cpu_grid.cpu_ship_placement()
        self.cpu_grid.display_game_board()
        self.take_player_shot()

    def place_ships(self):
        print('Begin by placing your 1x1 ships on the game board.\n')
        placed_ships = 0
        while placed_ships < 3:
            print(f'*** {3 - placed_ships} ships remaining ***\n')
            pos = Game.get_position_input('Position for your ship (i.e. "B2") ')
            # os.system('clear')
            if self.player_grid.query_position(pos[0], pos[1]) == 'S':
                self.player_grid.display_game_board()
                print('\nCannot place a ship on top of another!\n')
                continue
            self.player_grid.place_ship(pos[0], pos[1])
            placed_ships += 1
            self.player_grid.display_game_board()
        self.ships_placed = True

    @classmethod
    def get_position_input(cls, message):
        """Ensure player input is a valid two-character string like 'A1', case-insensitive.
        
        Parameters:
            message (str): display message for input field

        Return:
            str (length 2)
        """
        accepted = False
        while not accepted:
            value = input(message)
            result = ''
            if not len(value) == 2:
                print('Position must be two characters!')
                continue
            if value[0].upper() in 'ABCDE':
                result += value[0].upper()
            else:
                print('First value must be valid letter!')
                continue
            if value[1].isnumeric() and int(value[1]) <= 5:
                result += value[1]
            else:
                print('Second value must be a valid number!')
                continue
            accepted = True
        return result

    @classmethod
    def display_cpu(self):
        print("You Cannot Hide")
        return self.cpu_grid.display_game_board()
    
    ##------- Outline for Player Fire
    
    def take_player_shot(self):
        print('Aim your cannon')

        pos = self.get_position_input('Enter position to fire : ')
        row = pos[0]
        column = pos[1]
        if self.cpu_grid.query_position(row, column) in ['H', 'M']:
            print('You have already fired at this position. Try again!')
        
        else:
            result = self.cpu_grid.query_position(row, column)
            if result == 'S':
                print('Hit!')
                self.cpu_grid.change_grid(row, column, 'H')
            else:
                print('Miss!')
                self.cpu_grid.change_grid(row, column, 'M')
                
    
