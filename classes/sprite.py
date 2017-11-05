#! /usr/bin/env python3
# coding: utf-8


"""
The Sprite Class used in the MacGyver Maze.
3rd project of OC Python Developer Path.
Author: Loïc Mangin
"""


import pygame.display
from pygame.locals import *

from constants import *


class Sprite:
    """A Sprite instance has 4 attributes :
        - attributes 'line' and 'col' give the position of the sprite
        in relation to the 'tile' attribute of the Level;
        - attribute 'name' is the string used to represent the sprite
        in the 'tile' attribute of the Level;
        - attribute 'inventory' is a list containing the item(s)
        possessed by the sprite.
        """

    def __init__(self, name):
        """Create a Sprite instance.
        Initialize inventory with 3 strings 'slot'
        used to display it outside the labyrinth.
        """
        self.line = self.col = 1
        self.name = name
        self.inventory = ["slot", "slot", "slot"]

    def confront(self, opponent):
        """Resolve confrontation between the sprite and an opponent.
        The confrontation with Murdoc is
        the only case (actually) approached.
        """
        if opponent == "murdoc":
            if "syringe" in self.inventory:
                return "Victory !"
            else:
                return "Defeat !"
        else:
            return ""

    def display_inventory(self, lvl, window):
        """Display MacGyver inventory outside the labyrinth.
        If the 'syringe' is in the inventory,
        it is the only item displayed.
        Else, three item(s) / empty slot(s) are displayed.
        It is at the end of this function that is tested
        if MacGyver possess the 3 items to make the syringe.
        """
        if "syringe" in self.inventory:
            x = sprite_size * (16 + 1.5)
            y = sprite_size * (12 + 1)
            window.blit(lvl.style["syringe"], (x, y))
        else:
            i = 0
            for line in [12]:
                for col in [16, 17, 18]:
                    x_slot = sprite_size * (col + 1.5)
                    y_slot = sprite_size * (line + 1)
                    window.blit(lvl.style[self.inventory[i]], (x_slot, y_slot))
                    i += 1
        if "ether" in self.inventory and \
                "needle" in self.inventory and \
                "tube" in self.inventory:
            self.inventory = ["syringe"]
        pygame.display.flip()

    def move(self, lvl, key=None):
        """Change Sprite position and eventually collect stuff
        if the move is possible.
        Move is not possible if it will bring to a wall or
        to Murdoc (in this case, the confrontation is resolved).
        Return a string to determine if the game continue or not.
        """
        x = self.col
        y = self.line
        dx = dy = 0
        if key == K_UP and y > 0:
            dy = -1
        elif key == K_RIGHT and x < 14:
            dx = +1
        elif key == K_DOWN and y < 14:
            dy = +1
        elif key == K_LEFT and x > 0:
            dx = -1
        if lvl.tile[y + dy][x + dx] == "murdoc":
            return self.confront("murdoc")
        elif lvl.tile[y + dy][x + dx] != "#":
            self.search_stuff(lvl, y + dy, x + dx)
            lvl.tile[y][x] = '.'
            self.line = y + dy
            self.col = x + dx
            lvl.tile[self.line][self.col] = self.name
        return ""

    def put_in(self, lvl):
        """Place the sprite on an empty ground tile
        that is on the Level borders (an entry / exit).
        """
        self.line, self.col = lvl.find_entry()
        lvl.tile[self.line][self.col] = self.name

    def search_stuff(self, lvl, line, col):
        """Change inventory if there is an item on the ground.
        Item name take place of the first empty slot."""
        tile = lvl.tile[line][col]
        if tile in ["ether", "needle", "tube"]:
            i = 0
            while self.inventory[i] != "slot" and i < 4:
                i += 1
            self.inventory[i] = tile


if __name__ == "__main__":
    pass
