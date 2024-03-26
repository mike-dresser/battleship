class Ship:

    def __init__(self, coords):
        """Tracks ship position and damage
       
        Parameters:
            coords (list): a list of coordinates passed from Grid
                            (i.e. [A2, A3, A4])
            """
        self.coords = coords
        self.damage = self.build()

    def build(self):
        """Initialize ship with coordinates and health status 
        
        'S' is unharmed, 'x' will indicate hit"""
        result = {}
        for location in self.coords:
            result.update({location: 'S'})

    def take_hit(self, location):
        """Record a hit, check if ship is sunk
        
        Parameters:
            location(str): hit location, like 'A1'
        Return:
            bool:          False means not sunk
            """
        self.damage[location] = 'x'
        is_sunk = True
        for coord in self.damage.keys():
           if coord == 'S':
               is_sunk = False
        return is_sunk