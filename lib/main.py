"""
The game state is represented by a list of lists, where
each list is a row on the board.
grid = [
        [ ·, ·, ·, ·, · ],
        [ ·, ·, ·, ·, · ],
        [ ·, ·, ·, ·, · ],
        [ ·, ·, ·, ·, · ],
        [ ·, ·, ·, ·, · ],
        [ ·, ·, ·, ·, · ]
        ]

An individual square can be addressed grid[a][b] where a 
is the row index, and b is the column index.
"""

def create_new_grid():
    grid = [
            [ '·', '·', '·', '·', '·' ],
            [ '·', '·', '·', '·', '·' ],
            [ '·', '·', '·', '·', '·' ],
            [ '·', '·', '·', '·', '·' ],
            [ '·', '·', '·', '·', '·' ]
            ]
    return grid

def display_game_board(grid):
    """Render game grid with column and row labels as a text block"""
    column_labels = ['1', '2', '3', '4', '5']
    row_labels = ['A', 'B', 'C', 'D', 'E']

    output = '   '
    for label in column_labels:
        output += label + '|'
    output += '\n'

    row_counter = 0
    for row in grid:
        output += f'{row_labels[row_counter]}  '
        for grid_square in row:
            output += f'{grid_square} '
        output += '\n' 
        row_counter += 1
    return output

def change_grid(grid, row, column, symbol):
    """Change a grid square to a different symbol"""
    row_dict = { 'A': 0,
                    'B': 1,
                    'C': 2,
                    'D': 3,
                    'E': 4}
    grid[row_dict[row]][int(column) - 1] = symbol
    return grid
    
x = create_new_grid()
print(display_game_board(x))
change_grid(x, 'A', 1, 'X')
change_grid(x, 'B', 2, 'O')
print(display_game_board(x))
