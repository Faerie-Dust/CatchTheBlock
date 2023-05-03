from game_screen import GameScreen

import pygame
from pygame.locals import *

SCREEN = None

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((854, 480), RESIZABLE) # intentionally not holding a reference here

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)

            if event.type == VIDEORESIZE: # called initially as well
                SCREEN = GameScreen(*event.size)

        SCREEN.render()

        CELLS = 10 # CELLSxCELLS amount

        for y in range(CELLS):
            for x in range(CELLS):
                cell = pygame.Rect(x * (SCREEN.width / CELLS), y * (SCREEN.height / CELLS))

        pygame.display.flip()
