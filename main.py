import pygame, sys
from pygame.locals import *


#  Initialize program
pygame.init()


# Choose the FPS value
FramePerSec = pygame.time.Clock()
FPS = 30


# Setting up color objects
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((300, 300))

pygame.draw.circle(DISPLAYSURF, BLACK, (200, 50), 30)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
