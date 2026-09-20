"""Class Snake untuk game klasik."""

import pygame
from src import settings


class Snake:
    def __init__(self):
        # Posisi awal di tengah grid
        start_x = settings.GRID_WIDTH // 2
        start_y = settings.GRID_HEIGHT // 2
        self.body = [(start_x, start_y),
                     (start_x - 1, start_y),
                     (start_x - 2, start_y)]
        self.direction = (1, 0)   # (dx, dy)
        self.grow_flag = False

    def change_direction(self, new_dir):
        """Ubah arah, cegah gerakan balik ke badan sendiri."""
        dx, dy = self.direction
        ndx, ndy = new_dir
        # Cegah 180 derajat
        if (ndx, ndy) == (-dx, -dy):
            return
        self.direction = new_dir

    def move(self):
        """Gerakkan ular 1 langkah."""
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Cek tabrakan dinding
        if (new_head[0] < 0 or new_head[0] >= settings.GRID_WIDTH or
                new_head[1] < 0 or new_head[1] >= settings.GRID_HEIGHT):
            return False  # game over

        # Cek tabrakan dengan badan sendiri
        if new_head in self.body[:-1]:
            return False

        self.body.insert(0, new_head)

        if self.grow_flag:
            self.grow_flag = False
        else:
            self.body.pop()

        return True

    def grow(self):
        """Tandai ular untuk bertambah panjang."""
        self.grow_flag = True

    def draw(self, surface):
        """Gambar ular ke layar."""
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(
                x * settings.CELL_SIZE,
                y * settings.CELL_SIZE,
                settings.CELL_SIZE,
                settings.CELL_SIZE
            )
            color = settings.GREEN if i == 0 else settings.DARK_GREEN
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, settings.BLACK, rect, 1)

    def get_head(self):
        return self.body[0]