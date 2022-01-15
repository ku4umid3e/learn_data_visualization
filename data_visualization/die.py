from random import randint


class Die():
    """ Class representing one cube"""
    
    def __init__(self, num_sides=6):
        """by default, use a die with 6 faces"""
        self.num_sides = num_sides

    def roll(self):
        """Returns a random number between 1 and the number of faces."""
        return randint(1, self.num_sides)
