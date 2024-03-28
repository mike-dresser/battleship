
class Ship:

    def __init__(self, coords, grid_ref):
        """Tracks ship position and damage
       
        Parameters:
            coords (list): a list of coordinates passed from Grid
                            (i.e. [A2, A3, A4])
            """
        self.coords = self.build(coords)
        self.grid = grid_ref

    def build(self, coords):
        """Initialize dict of ship coordinates and health status 
        
        'S' is unharmed, 'x' indicates a hit"""
        coord_dict = {}
        for location in coords:
            coord_dict.update({location: 'S'})
        return coord_dict

    def survive_hit(self, location):
        """Record a hit, check if ship is sunk
        
        Parameters:
            location(str): hit location, like 'A1'
        Return:
            bool:   True == not sunk
            """
        from grid import Grid
        self.coords[location] = 'x'
        # Check self to see if undamaged spots remain
        for coord in self.coords:
            if self.coords[coord] == 'S':
                return True
        for pos in self.coords:
            self.grid.change_grid(pos[0], pos[1], '👻')
        return False