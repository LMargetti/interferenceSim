import pygame
import sys
import field
import wave

pygame.init()

# Screen Variables
black = (0, 0, 0)
grey = (50, 50, 50)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
world_width = 800
world_height = world_width

# Pygame Objects
screen = pygame.display.set_mode((world_width, world_height))
clock = pygame.time.Clock()
seconds_passed = (pygame.time.get_ticks()/1000)

# Field Grid
axis_squares = 80                                  # Number of squares
grid = field.Grid(axis_squares, world_width)

source = wave.Source(40, 40, 2, 16)
points = source.create_points(3, seconds_passed)

# Main Loop Variables
time = 0
fps = 60
dt = 1/fps
running = True


# Loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

    # Drawing Grid
    grid.draw_grid(screen)
    grid.update_grid()

    for pt in points:
        pt.update_pos(dt)
        pt_x = round(pt.pos[0])
        pt_y = round(pt.pos[1])
        grid.emit_colour(pt_x, pt_y, (255, 255, 255))

    # Updating Pygame and progressing time
    time += dt
    clock.tick(fps)
    pygame.display.update()
