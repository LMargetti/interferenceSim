import numpy as np
import pygame


class Field:
    def __init__(self, size):
        self.array = np.zeros((size, size))

    def update_index(self, update, index):
        self.array[index] = update
