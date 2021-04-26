import numpy as np
import pygame
import sys
import field_class

pygame.init()

# Screen Variables
screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Wave Simulation")

# Colour Variables
black = (0, 0, 0)
white = (255, 255, 255)
grey = (127, 127, 127)

# Timing Variables
time = 0
dt = 0.05

# Loop
running = True
while running:
    screen.fill(black)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Updating Pygame and progressing time
    time += dt
pygame.quit()
