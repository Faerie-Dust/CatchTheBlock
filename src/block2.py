import pygame
from pygame.locals import *
from pathlib import Path

class Block:
    IMAGE = None

    def __init__(self, assets_path: 'Path', rect: 'pygame.Rect'):
        Block.IMAGE = pygame.transform.smoothscale_by(pygame.image.load(Path(assets_path, "block.png")), 1 / 4)
        self._left, self._right = rect.left, rect.right

        self._x = rect.centerx - Block.IMAGE.get_width() / 2 # center of screen
        self.y = rect.top + 10 # offset from top to appear like its not at the very edge

        self._reverse = False

        self._animate = True
        self._falling = False

    def render(self, top: int):
        screen = pygame.display.get_surface()

        if self._animate:
            if not self._reverse:
                self._x += 1

                if self._x >= self._right - Block.IMAGE.get_width():
                    self._reverse = True
            else:
                self._x -= 1

                if self._x <= self._left:
                    self._reverse = False
        elif self._falling:
            self.y += 1

            if self.y + Block.IMAGE.get_height() == top:
                self._falling = False

        screen.blit(Block.IMAGE, (self._x, self.y))

    def stop_motion(self):
        self._animate = False
        self._falling = True

    def is_alive(self):
        return self._animate or self._falling
