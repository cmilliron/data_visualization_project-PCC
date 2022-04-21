from random import randint

class Die:
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        """Intial properies of die object. Default is a 6 sied die."""
        self.num_sides = num_sides

    def roll(self):
        """Return random value between 1 and the number of sides."""
        return randint(1, self.num_sides)
        
