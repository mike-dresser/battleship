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

    def display_game_board(self):
        """Render game grid with column and row labels as a text block"""
        column_labels = ['1', '2', '3', '4', '5']
        row_labels = ['A', 'B', 'C', 'D', 'E']
        output = '   '

        for label in column_labels:
            output += label + '|'
        output += '\n'
        row_counter = 0
        for row in self.state:
            output += f'{row_labels[row_counter]}  '
            for grid_square in row:
                output += f'{grid_square} '
            output += '\n' 
            row_counter += 1
        print(output)

    def change_grid(self, row, column, symbol):
        """Change a grid square to a different symbol
        
        Parameters:
            row (str):           a row by letter name (i.e. 'A')
            column (int | str):  a column number
            symbol (str):        the symbol to replace the grid square with

        Return value:
            None
        """
        row_dict = { 'A': 0,'B': 1,'C': 2,'D': 3,'E': 4}
        self.state[row_dict[row]][int(column) - 1] = symbol
        self.display_game_board()