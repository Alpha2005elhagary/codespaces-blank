import pygame
pygame.init()
window=pygame.display.set_mode((450,500))
clock=pygame.time.Clock()
rect=pygame.rect(42,56,30,30)
vel=5
run=True
while run:
    clock.tick(100)
    for event in pygame.event