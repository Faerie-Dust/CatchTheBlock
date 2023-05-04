import pygame, pathlib
from pygame.locals import *

direction = 1
falling = "false"
fallingStart = "false"

if __name__ == "__main__":
    pygame.init()

    _ASSETS_PATH = pathlib.Path(__file__).parent.parent.joinpath("assets")

    screen = pygame.display.set_mode((854, 480))
    block = pygame.image.load(pathlib.Path(_ASSETS_PATH, "jackolantern.png"))

    blockScale = pygame.transform.smoothscale(block, (block.get_width() / 10, block.get_height() / 10))

    pos_x = (screen.get_width() - blockScale.get_width()) / 2
    pos_y = 0 + blockScale.get_height()
    
    def blockMove(pos_x, pos_y, screen):
        global direction
        global falling
        global fallingStart
        keys_pressed = pygame.key.get_pressed()
        pos_x += (0.1 * direction)
        width = screen.get_width()
        height = screen.get_height()

        if pos_x >= width - blockScale.get_width() or pos_x <= 0:
            direction *= -1
        
        if fallingStart == "false":
            if keys_pressed[K_SPACE]:
                direction = 0
                falling = "true"
                fallingStart = "true"
        
        if falling == "true":
            if direction == 0:
                pos_y += 1
                if pos_y >= height - blockScale.get_height():
                    pos_y += 0
                    falling = "false" 

        return pos_x, pos_y

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)

        # rendering CODE GOES HERE
        screen.fill((0, 0, 0, 0))
        screen.blit(blockScale, (pos_x, pos_y))
        pos_x, pos_y = blockMove(pos_x, pos_y, screen)
        
        pygame.display.flip()