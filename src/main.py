from game_screen import GameScreen

import pygame
from pygame.locals import *

SCREEN = None

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((854, 480), RESIZABLE) # intentionally not holding a reference here

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)

            if event.type == VIDEORESIZE: # called initially as well
                SCREEN = GameScreen(*event.size)

        SCREEN.render()

        pygame.display.flip()
