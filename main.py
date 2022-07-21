import pygame
import sys

pygame.init()

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 600

FPS = 60
clock = pygame.time.Clock()

LIGHT_BLUE = (186, 228, 252)
PURPLE = (179, 117, 218)

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Jumping Rabbit")
screen.fill(LIGHT_BLUE)

surf_player = pygame.Surface((50, 80))
surf_player.fill(PURPLE)
rect_player = surf_player.get_rect(centerx=WINDOW_WIDTH//2, bottom=WINDOW_HEIGHT)

screen.blit(surf_player, rect_player)
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

    clock.tick(30)
