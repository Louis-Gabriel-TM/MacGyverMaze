#! /usr/bin/env python3
# coding: utf-8


"""
Graphic Constants used in The MacGyver Maze.
3rd project of OC Python Developer Path.

Author: Loïc Mangin

Most constants are paths to images files
"""

# number of files level "level_x.txt"
nb_of_levels = 3

# sprite_size determines the choice of images set used as sprites
# in the case (not actually used) of several existing images sets.
sprite_size = 48

# game window dimensions based on sprite_size
win_width = 22 * sprite_size
win_height = 17 * sprite_size

# images files
suffix = "_{}.png".format(str(sprite_size))
background_img = "images/background" + suffix
defeat_img = "images/defeat" + suffix
victory_img = "images/victory" + suffix
play_again_img = "images/play_again" + suffix

ground_img = "ground" + suffix
wall_img = "wall" + suffix

suffix = "_{}.png".format(str(sprite_size))
ether_img = "ether" + suffix
needle_img = "needle" + suffix
slot_img = "slot" + suffix
syringe_img = "syringe" + suffix
tube_img = "tube" + suffix

macgyver_img = "macgyver" + suffix
murdoc_img = "murdoc" + suffix
