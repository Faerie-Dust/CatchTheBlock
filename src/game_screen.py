import pygame
from pygame.locals import *

class GameScreen:
    _OUTER_COLOR = (96, 96, 96)
    _INNER_COLOR = (48, 48, 48)

    def __init__(self, width: int, height: int):
        length = min(width, height)

        # center coordinate on width/height depending which is larger
        pos_x = 0 if length == width else (width - length) / 2
        pos_y = 0 if length == height else (height - length) / 2

        self._rect = pygame.Rect(pos_x, pos_y, length, length)

        # expose for usage outside the class TODO: remove necessity
        self.top = self._rect.top
        self.left = self._rect.left
        self.width = self._rect.width
        self.height = self._rect.height

    def render(self):
        screen = pygame.display.get_surface()

        screen.fill(GameScreen._OUTER_COLOR)
        pygame.draw.rect(screen, GameScreen._INNER_COLOR, self._rect)
