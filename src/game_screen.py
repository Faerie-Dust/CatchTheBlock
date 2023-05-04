import pygame
from block2 import Block
from pathlib import Path
from pygame.locals import *

class GameScreen:
    _ASSETS_PATH = Path(__file__).parent.parent.joinpath("assets")

    _OUTER_COLOR = (96, 96, 96)
    _INNER_COLOR = (48, 48, 48)

    _BLOCKS = []

    def __init__(self, width: int, height: int):
        length = min(width, height)

        # center coordinate on width/height depending which is larger
        pos_x = 0 if length == width else (width - length) / 2
        pos_y = 0 if length == height else (height - length) / 2

        self._rect = pygame.Rect(pos_x, pos_y, length, length)
        self._platform = pygame.transform.smoothscale_by(pygame.image.load(Path(GameScreen._ASSETS_PATH, "platform.png")), 4 / 5)

    def render(self):
        screen = pygame.display.get_surface()

        screen.fill(GameScreen._OUTER_COLOR)
        pygame.draw.rect(screen, GameScreen._INNER_COLOR, self._rect)

        platform_rect = screen.blit(self._platform, (self._rect.centerx - self._platform.get_width() / 2, self._rect.bottom - self._platform.get_height() - 5))

        if len(GameScreen._BLOCKS) == 0 or not GameScreen._BLOCKS[-1].is_alive():
            GameScreen._BLOCKS.append(Block(GameScreen._ASSETS_PATH, self._rect))

        keys = pygame.key.get_pressed()

        if keys[K_SPACE]:
            GameScreen._BLOCKS[-1].stop_motion() # stop the most recent block and make it fall

        for block in GameScreen._BLOCKS:
            block.render(platform_rect.top - (len(GameScreen._BLOCKS) - 1) * Block.IMAGE.get_height())
