#! /usr/bin/env python3
# coding: utf-8


""" The Stuff class used in the MacGyver Maze game """


class Stuff:
    """ All things that MacGyver can collect or produce """

    def __init__(self, name):
        self.line = self.col = 0
        self.name = name

    def put_in(self, lvl):
        self.line, self.col = lvl.find_tile('.')
        lvl.tile[self.line][self.col] = self.name


if __name__ == "__main__":
    pass
