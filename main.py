import numpy as np
import pygame
import finite_difference
import field

pygame.init()

# Screen Variables
screen_size = (640, 640)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Wave Simulation")

# Colour Variables
black = (0, 0, 0)
white = (255, 255, 255)
grey = (127, 127, 127)

# Physical Variables
time = 0
dt = 0.05
c = 344     # Wave Speed
squares = 80    # Number of squares on an axis
field_size = 640
fabric = field.Grid(80, field_size)

fabric.emit_colour(40, 40, white)

past_fab = field.Grid(80, field_size)

# Loop
running = True
while running:

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fabric.update_grid(c, dt, past_fab.grid)
    fabric.draw_grid(screen)
    # Updating Pygame and progressing time
    past_fab = fabric
    time += dt
pygame.quit()
