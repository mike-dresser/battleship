"""
The game state is represented by a list of lists, where
each list is a row on the board.
grid = [
        [ o, o, o, o, o ],
        [ o, o, o, o, o ],
        [ o, o, o, o, o ],
        [ o, o, o, o, o ],
        [ o, o, o, o, o ],
        [ o, o, o, o, o ]
        ]

An individual square can be addressed grid[a][b] where a 
is the row index, and b is the column index.
"""


grid = [
        [ 'o', 'o', 'o', 'o', 'o' ],
        [ 'o', 'o', 'o', 'o', 'o' ],
        [ 'o', 'o', 'o', 'o', 'o' ],
        [ 'o', 'o', 'o', 'o', 'o' ],
        [ 'o', 'o', 'o', 'o', 'o' ]
        ]

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

print(display_game_board(grid))     