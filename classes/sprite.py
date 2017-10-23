#! /usr/bin/env python3
# coding: utf-8


""" The Sprite class used in the MacGyver Maze """


import pygame.display
from pygame.locals import *

from constants import *


class Sprite:
    """  """

    def __init__(self, name):
        """  """
        self.line = self.col = 1
        self.name = name
        self.inventory = ["slot", "slot", "slot"]

    def confront(self, opponent):
        """  """
        if opponent == "murdoc":
            if "syringe" in self.inventory:
                return "Victory !"
            else:
                return "Defeat !"
        else:
            return ""

    def display_inventory(self, lvl, window):
        """  """
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
        """  """
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
        """  """
        self.line, self.col = lvl.find_entry()
        lvl.tile[self.line][self.col] = self.name

    def search_stuff(self, lvl, line, col):
        """  """
        tile = lvl.tile[line][col]
        if tile in ["ether", "needle", "tube"]:
            i = 0
            while self.inventory[i] != "slot" and i < 4:
                i += 1
            self.inventory [i] = tile


if __name__ == "__main__":
    pass
