#! /usr/bin/env python3
# coding: utf-8


""" The Level class used in the MacGyver Maze game """


from random import randint

import pygame.display

from constants import *


class Level:
    """  """

    def __init__(self, file_name, design="random"):
        """  """
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
        """  """
        if design == "random":
            avalaible = ["blue_stone", "brown_stone"]
            design_index = randint(0, len(avalaible) - 1)
            design = avalaible[design_index]
        folder = "images/{}/".format(design)
        self.style = {
            ".": pygame.image.load(folder + ground_img).convert(),
            "#": pygame.image.load(folder + wall_img).convert()
            }

    def design_stuff(self):
        """  """
        folder = "images/stuff/"
        self.style["ether"] = pygame.image.load(folder + ether_img).convert_alpha()
        self.style["needle"] = pygame.image.load(folder + needle_img).convert_alpha()
        self.style["slot"] = pygame.image.load(folder + slot_img).convert_alpha()
        self.style["syringe"] = pygame.image.load(folder + syringe_img).convert_alpha()
        self.style["tube"] = pygame.image.load(folder + tube_img).convert_alpha()
        for stuff in self.style:
            self.style[stuff].set_colorkey((255, 255, 255))

    def design_sprite(self):
        """  """
        folder = "images/sprites/"
        self.style["macgyver"] = pygame.image.load(folder + macgyver_img).convert_alpha()
        self.style["murdoc"] = pygame.image.load(folder + murdoc_img).convert_alpha()

    def display(self, window):
        """  """
        for line in range(15):
            for col in range(15):
                x_tile = 48 * (col + 1)
                y_tile = 48 * (line + 1)
                tile_type = self.tile[line][col]
                window.blit(self.style[tile_type], (x_tile, y_tile))
        pygame.display.flip()

    def find_entry(self):
        """  """
        for line in [0, 14]:
            for col in range(1, 13):
                if self.tile[line][col] == '.':
                    return line, col
        for col in [0, 14]:
            for line in range(1, 13):
                if self.tile[line][col] == '.':
                    return line, col

    def find_tile(self, tile_type):
        """  """
        line = col = 0
        while self.tile[line][col] != tile_type:
            line = randint(0, 14)
            col = randint(0, 14)
        return line, col

    def load_level(self, file_name):
        """  """
        with open(file_name, "r") as lvl_file:
            for line in range(15):
                self.tile[line] = lvl_file.readline().strip().split(" ")


if __name__ == "__main__":
    pass
