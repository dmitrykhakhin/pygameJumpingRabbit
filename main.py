import pygame
import sys

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()

# git test
