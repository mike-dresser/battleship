import random
from ship import Ship

class Grid:

    SHIP_SIZE = 1

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
        self.x_ray = True #show ship positions as 'S'
        self.ships = []

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
    
    def valid_ship_placement(self, coord, horizontal, length):
        """Return whether the ship can be placed without overlapping another or leaving the board.
         
        Parameters:
            coord       (str): point marking the prow of the ship ("A1")
            horizontal (bool): orientation; True == horizontal
            length      (int): ship length defined in Game
        Return:
            Boolean (True == valid position)
            """
        row, column = coord[0], coord[1]
        if not horizontal:
            #check vertical alignment
            for i in range(length):
                if self.row_dict[row] + i > 4:
                    return False
                if self.state[self.row_dict[row] + i][int(column) - 1] == 'S':
                    return False
            return True        
        else:
            # Check horizontal alignment
            for i in range(length):
                if int(column) + i > 5:
                    return False
                if self.state[self.row_dict[row]][int(column) - 1 + i] == 'S':
                    return False
            return True        

    
    def place_ship(self, start_coords, horizontal):
        """Place a ship on game grid, create ship instance
        
        Parameters:
            start_coords (str): string like "A1." Further coordinates are calculated from this position based on ship length and orientation.

        Return:
            None
        """
        # Calculate all coordinates occupied by ship
        coords =[start_coords]
        count = 1
        while count < Grid.SHIP_SIZE:
            if not horizontal:
                coords.append(self.row_labels[self.row_dict[start_coords[0]] + count ] + start_coords[1])
                count += 1
            else:
                coords.append(start_coords[0] + str(int(start_coords[1]) + count))
                count += 1
    
        # Update grid state
        for coord in coords:
            row = coord[0]
            column = coord[1]

            self.state[self.row_dict[row]][int(column) - 1] = 'S'
        # Build new ship object
        new = Ship(coords) 
        self.ships.append(new)

    def display_game_board(self):
        """Render game grid with column and row labels into a text block"""     
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
        """Make ship positions visible with 'S'
        
        This is always ON for the user, and begins OFF for CPU"""
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
        """Randomly place ships on the game grid"""
        # ship_sizes = [2, 3, 1] 
        # total_ships = sum(ship_sizes)
        total_ships = 3
        # Place ships randomly
        placed_ships = 0
        while placed_ships < total_ships:
            row = random.choice(self.row_labels)
            column = random.choice(self.column_labels)
            horizontal = random.choice([True, False])
            # hard-coding ship length below for now, user ship placement is called from Game where length is store, but CPU placement is here
            if self.valid_ship_placement(row + column, horizontal, Grid.SHIP_SIZE):
                self.place_ship(row + column, horizontal)
                placed_ships += 1

    def query_position(self, row, column):
            """Return the current value for a grid position"""
            return self.state[self.row_dict[row]][int(column) - 1]
    
    def fire_on(self, row, column):
        """Recieve fire, update grid
        
        Return:
            str: 'S' | '🌊'
            """
        result = self.query_position(row, column)
        if result == 'S':    
            self.change_grid(row, column, '💥')
            self.assign_damage(row, column)
        else:
            self.change_grid(row, column, '💦')
        return result

    def assign_damage(self, row, column):
        """Assign damage to ships, remove from list if sunk
        
        Return:
            None"""
        coord = row + column
        for ship in self.ships:
            if ship.coords.get(coord):
                if ship.survive_hit(coord):
                    return
                else:
                    self.ships.remove(ship)
