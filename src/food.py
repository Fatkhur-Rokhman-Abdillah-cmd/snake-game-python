"""Class Food untuk game Snake."""

import random
import pygame
from src import settings


class Food:
    def __init__(self, snake_body=None):
        self.position = (0, 0)
        self.randomize(snake_body or [])

    def randomize(self, snake_body):
        """Letakkan makanan pada posisi acak yang tidak ditempati ular."""
        empty_cells = [
            (x, y)
            for x in range(settings.GRID_WIDTH)
            for y in range(settings.GRID_HEIGHT)
            if (x, y) not in snake_body
        ]
        if empty_cells:
            self.position = random.choice(empty_cells)

    def draw(self, surface):
        x, y = self.position
        rect = pygame.Rect(
            x * settings.CELL_SIZE,
            y * settings.CELL_SIZE,
            settings.CELL_SIZE,
            settings.CELL_SIZE
        )
        pygame.draw.rect(surface, settings.RED, rect)
        pygame.draw.rect(surface, settings.BLACK, rect, 1)