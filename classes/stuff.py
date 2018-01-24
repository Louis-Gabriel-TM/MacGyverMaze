#! /usr/bin/env python3
# coding: utf-8


"""
The Stuff class used in the MacGyver Maze game.
3rd project of OC Python Developer Path.

Author: Loïc Mangin
"""


class Stuff:
    """A Stuff instance has 3 attributes :
        - attributes 'line' and 'col' give the position of the item
        in relation to the 'tile' attribute of the Level;
        - attribute 'name' is the string used to represent the item
        in the 'tile' attribute of the Level.
    """

    def __init__(self, name):
        """Create a Stuff instance."""
        self.line = self.col = 0
        self.name = name

    def put_in(self, lvl):
        """Randomly place the item on an empty ground tile."""
        self.line, self.col = lvl.find_tile('.')
        lvl.tile[self.line][self.col] = self.name


if __name__ == "__main__":
    pass
