import numpy as np
import pygame
import finite_difference


class Grid:
    def __init__(self, num_squares, size):
        self.grid = np.zeros((num_squares, num_squares, 3))     # 3 is for colour (r, g, b)
        self.sqr_size = size/num_squares
        self.num_sqrs = num_squares
        self.x_axis = self.grid[0]
        self.y_axis = self.grid[1]

    def draw_grid(self, surface):
        for x in range(self.num_sqrs):
            for y in range(self.num_sqrs):
                if self.grid[x][y].sum() != 0:
                    x_pos = x * self.sqr_size
                    y_pos = y * self.sqr_size
                    rect = pygame.Rect(x_pos, y_pos, self.sqr_size, self.sqr_size)
                    pygame.draw.rect(surface, self.grid[x][y], rect)

    def update_grid(self, c, dt, past_field, force_field=0):
        finite_difference.approx_field(c, dt, self.sqr_size, self.grid, past_field, force_field)

    def update_pixel(self, x, y, pxl_colour):
        self.grid[x][y] = pxl_colour

    def emit_colour(self, x, y, pxl_colour):
        colour = np.array(pxl_colour)
        self.grid[x][y] = colour
