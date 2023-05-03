from pathlib import Path
from game_screen import GameScreen

import pygame
from pygame.locals import *

ASSETS_PATH = Path(__file__).parent.parent.joinpath("assets")

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((854, 480), RESIZABLE) # intentionally not holding a reference here

    screen = GameScreen(*pygame.display.get_window_size())
    platform = pygame.transform.smoothscale_by(pygame.image.load(Path(ASSETS_PATH, "platform.png")), 4 / 5)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)

            if event.type == VIDEORESIZE: # called initially as well
                screen = GameScreen(*event.size)

        screen.render()

        pygame.display.get_surface().blit(platform, ((screen.width - platform.get_width()) / 2, screen.bottom - platform.get_height() - 5))

        pygame.display.flip()
