import pygame
import sys

pygame.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

FPS = 60

LIGHT_BLUE = (186, 228, 252)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jumping Rabbit")
screen.fill(LIGHT_BLUE)

clock = pygame.time.Clock()

pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    clock.tick(30)
