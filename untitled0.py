import pygame
from pygame.locals import *
import sys

pygame.init()
windows = pygame.display.set_mode((750, 800), 32)
pygame.display.set_caption("fire arms")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
move_x = 200
move_y = 200

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:  # Fixed here
                move_x -= 30
            if event.type == pygame.K_RIGHT:
                move_x += 20
    windows.fill(WHITE)
    pygame.draw.line(windows, BLUE, (move_x, move_y), (move_x, move_y), 100)
    pygame.display.update()



