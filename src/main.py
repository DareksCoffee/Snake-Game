import pygame # Import the Pygame library. For more information, visit https://pygame.org.
from snake import startgame

"""
    function startgame()

    Parameters:
    - screen (pygame.Surface): The Pygame screen surface.
    - screen_width (int): The width of the game screen.
    - screen_height (int): The height of the game screen.
    - clock (pygame.time.Clock): The Pygame clock object.

    Returns:
    None
"""


pygame.init() # Initialize pygame

## GLOBAL WINDOW VARIABLES ##
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
#############################

clock = pygame.time.Clock()

## START GAME ##
startgame(screen, screen_height, screen_width, clock)
print("Snake game has started!")
################