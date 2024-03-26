import random

class Grid:
    """
    The game grid is represented as a list of lists,
    with each sub-list as a row. An individual cell
    can be addressed as grid[a][b].

           1|2|3|4|5|
        A  · · · · · 
        B  · · · · · 
        C  · · · · · 
        D  · · · · · 
        E  · · · · · 

    Next goal will be to create a grid of arbitrary size, 
    with appropriate labels!
    """

    def __init__(self) -> None:
        self.state = Grid.reset_grid()
        self.column_labels = ['1', '2', '3', '4', '5'] # subtracting 1 gets the sub-list index
        self.row_labels = ['A', 'B', 'C', 'D', 'E']
        self.row_dict = { 'A': 0,'B': 1,'C': 2,'D': 3,'E': 4} # convert row letters to indexes
        self.x_ray = True #show ship positions

    @classmethod
    def reset_grid(cls):
        """Set game state to starting position"""
        grid = [
                [ '🌊', '🌊', '🌊', '🌊', '🌊' ],
                [ '🌊', '🌊', '🌊', '🌊', '🌊' ],
                [ '🌊', '🌊', '🌊', '🌊', '🌊' ],
                [ '🌊', '🌊', '🌊', '🌊', '🌊' ],
                [ '🌊', '🌊', '🌊', '🌊', '🌊' ]
                ]
        return grid
    
    def valid_ship_placement(self, coord, length):
        """Return whether the ship can be placed without overlapping another or leaving the board.
         
        Parameters:
            coord (str): point marking the prow of the ship ("A1")
            length (int): global ship length defined in Game
        Return:
            Boolean (True == valid)
            """
        row, column = coord[0], coord[1]
        for i in range(length):
            if self.row_dict[row] + i > 4:
                return False
            if self.state[self.row_dict[row] + i][int(column) - 1] == 'S':
                return False
        return True        

    
    def place_ship(self, start_coords):
        """Place a ship on game grid
        
        Parameters:
            row (str):        row letter
            column(int|str):  column number

        Return:
            None
        """
        coords =[start_coords,
                self.row_labels[self.row_dict[start_coords[0]] + 1 ] + start_coords[1]
        ]
        for [row, column] in coords:
            self.state[self.row_dict[row]][int(column) - 1] = 'S'

    def display_game_board(self):
        """Render game grid with column and row labels as a text block"""     
        output = '   '
        for label in self.column_labels:
            output += label + ' |'
        output += '\n'
        row_counter = 0
        for row in self.state:
            output += f'{self.row_labels[row_counter]}  '
            for grid_square in row:
                if self.x_ray:
                    output += f'{grid_square} '
                    if grid_square == 'S': #emoji is 2 rows wide, add padding
                        output += ' '
                else:
                    if grid_square == 'S':
                        output += '🌊 '
                    else:    
                        output += f'{grid_square} '
            output += '\n' 
            row_counter += 1
        return output
    
    def toggle_ship_visibility(self):
        self.x_ray = not self.x_ray
            
    def change_grid(self, row, column, symbol):
        """Change a grid square to a different symbol
        
        Parameters:
            row (str):         row by letter name (i.e. 'A')
            column (int|str):  column number
            symbol (str):      the symbol to replace the grid square with

        Return:
            None
        """
        
        self.state[self.row_dict[row]][int(column) - 1] = symbol

    def cpu_ship_placement(self):
        """Randomly place ships on the game grid
        
        NEXT GOAL WOULD BE TO HIDE THE SHIPS OR UNLESS HIT
        
        """

        # ship_sizes = [2, 3, 1] 
        # total_ships = sum(ship_sizes)
        total_ships = 3
        # Place ships randomly
        placed_ships = 0
        while placed_ships < total_ships:
            row = random.choice(self.row_labels)
            column = random.choice(self.column_labels)
            # hard-coding ship length below for now, user ship placement is called from Game where length is store, but CPU placement is here
            if self.valid_ship_placement(row + column, 2):
                self.place_ship(row + column)
                placed_ships += 1

    def query_position(self, row, column):
            """Return the current value for a grid position"""
            return self.state[self.row_dict[row]][int(column) - 1]
    



# player_grid = Grid()
# cpu_grid = Grid()

# # Place ships for the CPU
# cpu_grid.cpu_ship_placement()

# # Display player's grid
# print("Player's Grid:")
# player_grid.display_game_board()

# # Display CPU's grid
# print("\nCPU's Grid:")
# cpu_grid.display_game_board()

# # print(cpu_grid)