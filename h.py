import pygame
pygame.init()
screen = pygame.display.set_mode((450, 350))
pygame.display.set_caption("fire arms")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
x = 100
y = 200
width = 50
height = 50
rect = pygame.Rect(x, y, width, height)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLACK)
    pygame.draw.rect(screen,RED, rect)
    pygame.display.flip()
pygame.quit()