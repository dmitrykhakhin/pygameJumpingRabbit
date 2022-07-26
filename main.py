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

    screen.fill(LIGHT_BLUE)
    screen.blit(surf_player, rect_player)
    pygame.display.update()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and rect_player.left > 0:
        rect_player.x -= 3
    elif keys[pygame.K_RIGHT] and rect_player.right < WINDOW_WIDTH:
        rect_player.x += 3

    clock.tick(30)
