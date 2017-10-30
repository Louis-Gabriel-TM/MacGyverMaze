#! /usr/bin/env python3
# coding: utf-8


"""
The MacGyver Maze, a 2D labyrinth game
3rd project of OC Python developer path
Author : Loïc Mangin
"""

import pygame.display

from classes.level import *
from classes.sprite import *
from classes.stuff import *
from constants import *


def end_game(event, window):
    """  """
    if event == "Victory !":
        panel = pygame.image.load(victory_img).convert()
    elif event == "Defeat !":
        panel = pygame.image.load(defeat_img).convert()
    x_panel = sprite_size * 4.5
    y_panel = sprite_size * 5.5
    window.blit(panel, (x_panel, y_panel))
    pygame.display.flip()


def init_display(width, height, back_img):
    """  """
    pygame.init()
    window = pygame.display.set_mode((width, height))
    background = pygame.image.load(back_img).convert()
    window.blit(background, (0, 0))
    return window


def init_maze(lvl_nb=1, random_lvl=True, design="random"):
    """  """
    if random_lvl:
        lvl_nb = randint(1, nb_of_levels)
    lvl_file = "levels/level_" + str(lvl_nb) + ".txt"
    return Level(lvl_file, design)


def init_stuff(lvl):
    """  """
    ether = Stuff("ether")
    needle = Stuff("needle")
    tube = Stuff("tube")
    ether.put_in(lvl)
    needle.put_in(lvl)
    tube.put_in(lvl)


def play_again(window):
    """  """
    panel = pygame.image.load(play_again_img).convert()
    x_panel = sprite_size * 4.5
    y_panel = sprite_size * 8.5
    window.blit(panel, (x_panel, y_panel))
    pygame.display.flip()
    no_choice = True
    while no_choice:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_o:
                    return True
                elif event.key == K_n:
                    return False


def main():
    """  """
    # Initialisation and displaying of the game window
    game_window = init_display(win_width, win_height, background_img)
    pygame.display.flip()
    # Initialisation of the maze
    maze = init_maze()
    maze.display(game_window)
    # Initialisation of the stuff
    init_stuff(maze)
    maze.design_stuff()
    # Initialisation of MacGyver and Murdoc
    macgyver = Sprite("macgyver")
    murdoc = Sprite("murdoc")
    macgyver.put_in(maze)
    murdoc.put_in(maze)
    maze.design_sprite()
    # Displaying the maze, stuff and sprites
    maze.display(game_window)
    macgyver.display_inventory(maze, game_window)
    # Game loop
    playing_game = True
    while playing_game:
        for event in pygame.event.get():
            if event.type == QUIT:
                playing_game = False
            elif event.type == KEYDOWN:
                confront_result = macgyver.move(maze, event.key)
                if confront_result != "":
                    end_game(confront_result, game_window)
                    playing_game = play_again(game_window)
                    if playing_game:
                        main()
                else:
                    maze.display(game_window)
                    macgyver.display_inventory(maze, game_window)


if __name__ == "__main__":
    main()
