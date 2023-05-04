from game_screen import GameScreen

import pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((854, 480), RESIZABLE) # intentionally not holding a reference here

    screen = GameScreen(*pygame.display.get_window_size())

    block_width = screen.width / 4
    block_height = screen.height / 20 # 20 blocks

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)

            if event.type == VIDEORESIZE: # called initially as well
                screen = GameScreen(*event.size)
                block_width = screen.width / 4
                block_height = screen.height / 20 # 20 blocks

        screen.render()

        #pygame.draw.rect(pygame.display.get_surface(), (255, 255, 255), pygame.Rect(platform_rect.centerx - block_width / 2, platform_rect.top - block_height, block_width, block_height))

        pygame.display.flip()
