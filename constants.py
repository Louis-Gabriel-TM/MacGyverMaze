#! /usr/bin/env python3
# coding: utf-8


"""  """

# number of files level "level_x.txt"
nb_of_levels = 3

# sprite size determines window dimensions
sprite_size = 48

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
