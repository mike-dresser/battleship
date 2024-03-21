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
        self.state = type(self).reset_grid()
        self.column_labels = ['1', '2', '3', '4', '5']
        self.row_labels = ['A', 'B', 'C', 'D', 'E']
        self.row_dict = { 'A': 0,'B': 1,'C': 2,'D': 3,'E': 4} # convert row letters to indexes

    @classmethod
    def reset_grid(cls):
        """Set game state to starting position"""
        grid = [
                [ '·', '·', '·', '·', '·' ],
                [ '·', '·', '·', '·', '·' ],
                [ '·', '·', '·', '·', '·' ],
                [ '·', '·', '·', '·', '·' ],
                [ '·', '·', '·', '·', '·' ]
                ]
        return grid
    
    def place_ship(self, row, column):
        """Place a ship on game grid
        
        Parameters:
            row (str):        row letter
            column(int|str):  column number

        Return:
            None
        """
        self.state[self.row_dict[row]][int(column) - 1] = 'S'

    def display_game_board(self):
        """Render game grid with column and row labels as a text block"""     
        output = '   '
        for label in self.column_labels:
            output += label + '|'
        output += '\n'
        row_counter = 0
        for row in self.state:
            output += f'{self.row_labels[row_counter]}  '
            for grid_square in row:
                output += f'{grid_square} '
            output += '\n' 
            row_counter += 1
        print(output)

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
        self.display_game_board()