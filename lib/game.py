from grid import Grid
import os

class Game:
    """Class to represent the current game"""

    def __init__(self):
        self.ships_placed = False
        self.game_over = False
        self.player_grid = Grid()
    
    def play(self):
        """Begin new game"""

        print('~ ~ ~  B A T T L E S H I P  ~ ~ ~\n\n')
        print('The year is 2024. Oceans are battlefields.')
    
        self.player_grid.display_game_board()
        self.place_ships()

    def place_ships(self):
        print('Begin by placing your 1x1 ships on the game board.\n')
        placed_ships = 0
        while placed_ships < 3:
            print(f'{3 - placed_ships} remaining.\n')
            pos = Game.get_position_input('Position for your ship (i.e. "B2") ')
            os.system('clear')

            self.player_grid.place_ship(pos[0], pos[1])
            placed_ships += 1
            self.player_grid.display_game_board()
        self.ships_placed = True

    @classmethod
    def get_position_input(cls, message):
        """Ensure player input is a valid position
        
        Parameters:
            message (str): be a two-character string like 'A1', case-insensitive.
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


    
