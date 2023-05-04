import pygame
from pathlib import Path
from pygame.locals import *
from pathlib import Path

class GameScreen:
    _ASSETS_PATH = Path(__file__).parent.parent.joinpath("assets")

    _OUTER_COLOR = (96, 96, 96)
    _INNER_COLOR = (48, 48, 48)

    def __init__(self, width: int, height: int):
        length = min(width, height)

        # center coordinate on width/height depending which is larger
        pos_x = 0 if length == width else (width - length) / 2
        pos_y = 0 if length == height else (height - length) / 2

        self._rect = pygame.Rect(pos_x, pos_y, length, length)
        self.platform = pygame.transform.smoothscale_by(pygame.image.load(Path(GameScreen._ASSETS_PATH, "platform.png")), 4 / 5)

        # expose for usage outside the class TODO: remove necessity
        self.top = self._rect.top
        self.left = self._rect.left
        self.width = self._rect.width
        self.height = self._rect.height
        self.bottom = self._rect.bottom
        self.centerx = self._rect.centerx

    def render(self):
        screen = pygame.display.get_surface()

        screen.fill(GameScreen._OUTER_COLOR)
        pygame.draw.rect(screen, GameScreen._INNER_COLOR, self._rect)

        platform_rect = screen.blit(self.platform, (self._rect.centerx - self.platform.get_width() / 2, self._rect.bottom - self.platform.get_height() - 5))
