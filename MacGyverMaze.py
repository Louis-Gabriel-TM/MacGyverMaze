#! /usr/bin/env python3
# coding: utf-8


"""
The MacGyver Maze, a 2D labyrinth game.
3rd project of OC Python Developer Path.

Author: Loïc Mangin
"""

import pygame
from pygame.locals import *


from classes.level import *
from classes.sprite import *
from classes.stuff import *
from MGM_constants import *


def end_game(event, window):
    """Use 'event' value to display a panel showing the
    result (Victory or Defeat) of the final confrontation.
    """
    panel = None
    if event == "Victory !":
        panel = pygame.image.load(victory_img).convert()
    elif event == "Defeat !":
        panel = pygame.image.load(defeat_img).convert()
    x_panel = sprite_size * 4.5
    y_panel = sprite_size * 5.5
    window.blit(panel, (x_panel, y_panel))
    pygame.display.flip()


def init_display(width, height, back_img):
    """Initialize Pygame.
    Return the game window with its background image.
    """
    pygame.init()
    window = pygame.display.set_mode((width, height))
    background = pygame.image.load(back_img).convert()
    window.blit(background, (0, 0))
    return window


def init_maze(lvl_nb=1, random_lvl=True, design="random"):
    """Initialize the labyrinth.
    Return a Level instance based on:
        - a chosen or (default) randomly selected .txt file;
        - a chosen or (default) randomly selected graphic design.
    """
    if random_lvl:
        lvl_nb = randint(1, nb_of_levels)
    lvl_file = "levels/level_" + str(lvl_nb) + ".txt"
    return Level(lvl_file, design)


def init_stuff(lvl):
    """Define the items (Stuff instances)
    and randomly spread them in the labyrinth.
    """
    ether = Stuff("ether")
    needle = Stuff("needle")
    tube = Stuff("tube")
    ether.put_in(lvl)
    needle.put_in(lvl)
    tube.put_in(lvl)


def play_again(window):
    """Display a 'Play again' panel and wait for an answer.
    Return 'True' to continue with another game,
    'False' to close the game.
    """
    panel = pygame.image.load(play_again_img).convert()
    x_panel = sprite_size * 4.5
    y_panel = sprite_size * 8.5
    window.blit(panel, (x_panel, y_panel))
    pygame.display.flip()
    no_choice = True
    while no_choice:
        pygame.time.Clock().tick(24)  # Maximum 24 loops by second
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_o:
                    return True
                elif event.key == K_n:
                    return False


def main():
    """Core code of the MacGyver Maze."""

    # Initialisation and displaying of the game window
    game_window = init_display(win_width, win_height, background_img)
    pygame.display.flip()
    # Initialisation and displaying of the maze
    maze = init_maze()
    maze.display(game_window)
    # Initialisation of the stuff
    init_stuff(maze)
    maze.design_stuff()
    # Initialisation of the sprites MacGyver and Murdoc
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
        pygame.time.Clock().tick(24)  # Maximum 24 loops by second
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                playing_game = False
            elif event.type == KEYDOWN:
                confront_result = macgyver.move(maze, event.key)
                if confront_result != "":  # If MacGyver confront to Murdock
                    end_game(confront_result, game_window)
                    playing_game = play_again(game_window)
                    if playing_game:
                        main()
                else:
                    maze.display(game_window)
                    macgyver.display_inventory(maze, game_window)


if __name__ == "__main__":
    main()
