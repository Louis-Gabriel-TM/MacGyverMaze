#! /usr/bin/env python3
# coding: utf-8


"""
The Level class used in the MacGyver Maze game.
3rd project of OC Python Developer Path.

Author: Loïc Mangin
"""


from random import randint

import pygame.display

from MGM_constants import *


class Level:
    """A Level instance has two attributes:
        - attribute 'tile' is a list of 15 lists, each containing
        15 strings (or simple characters) describing one of
        the 15 * 15 squares composing the labyrinth;
        - attribute 'style' is a dictionary that associates
        each string or character to the image used for the display.
    """

    def __init__(self, file_name, design):
        """Create a Level instance.
        Attribute 'tile' is loaded from file_name, a .txt file.
        Attribute 'style' can be chosen or randomly selected depending 'design' value.
        """
        self.tile = [["."] * 15] * 15
        self.load_level(file_name)
        self.style = dict()
        self.design_level(design)

    def char_display(self):
        """ DEBUG """
        print()
        for line in range(15):
            print(" ".join(self.tile[line]))

    def design_level(self, design):
        """Define the initial content of 'style' attribute :
        the images for wall tile ('#') and ground tile ('.').
        """
        if design == "random":
            avalaible = ["blue_stone", "brown_stone"]
            design_index = randint(0, len(avalaible) - 1)
            design = avalaible[design_index]
        folder = "images/{}/".format(design)
        self.style = {
            ".": pygame.image.load(folder + ground_img).convert(),
            "#": pygame.image.load(folder + wall_img).convert()
            }

    def design_sprite(self):
        """Add to the 'style' attribute the images
        for the sprites MacGyver and Murdoc.
        """
        folder = "images/sprites/"
        self.style["macgyver"] = pygame.image.load(folder + macgyver_img).convert_alpha()
        self.style["murdoc"] = pygame.image.load(folder + murdoc_img).convert_alpha()

    def design_stuff(self):
        """Add to the 'style' attribute the images
        for the items in the labyrinth and MacGyver inventory."""
        folder = "images/stuff/"
        self.style["ether"] = pygame.image.load(folder + ether_img).convert_alpha()
        self.style["needle"] = pygame.image.load(folder + needle_img).convert_alpha()
        self.style["slot"] = pygame.image.load(folder + slot_img).convert_alpha()
        self.style["syringe"] = pygame.image.load(folder + syringe_img).convert_alpha()
        self.style["tube"] = pygame.image.load(folder + tube_img).convert_alpha()

    def display(self, window):
        """Display the labyrinth described by the 'tile' attribute,
        using the images in the 'style' attribute.
        """
        for line in range(15):
            for col in range(15):
                x_tile = sprite_size * (col + 1)
                y_tile = sprite_size * (line + 1)
                tile_type = self.tile[line][col]
                window.blit(self.style[tile_type], (x_tile, y_tile))
        pygame.display.flip()

    def find_entry(self):
        """Travel along the Level border to find an ground tile
        (an entry / exit) and return its position.
        """
        for line in [0, 14]:
            for col in range(1, 13):
                if self.tile[line][col] == '.':
                    return line, col
        for col in [0, 14]:
            for line in range(1, 13):
                if self.tile[line][col] == '.':
                    return line, col

    def find_tile(self, tile_type):
        """Choose randomly a tile of the Level and
        return its position only if it is
        a 'tile_type' tile.
        """
        line = col = 0
        while self.tile[line][col] != tile_type:
            line = randint(0, 14)
            col = randint(0, 14)
        return line, col

    def load_level(self, file_name):
        """Define the initial content of the 'tile' attribute.
        The .txt file used, file_name here, only contains
        15 *15 characters '#' (for a wall tile) or
        '.' (for a ground tile), separated by spaces.
        """
        with open(file_name, "r") as lvl_file:
            for line in range(15):
                self.tile[line] = lvl_file.readline().strip().split(" ")


if __name__ == "__main__":
    pass
