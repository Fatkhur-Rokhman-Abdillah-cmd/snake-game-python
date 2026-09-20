"""Fungsi utilitas untuk game."""

import sys
import pygame
from src import settings


def draw_text(surface, text, size, color, x, y, center=False):
    """Menggambar teks di layar."""
    font = pygame.font.SysFont("arial", size, bold=True)
    rendered = font.render(text, True, color)
    rect = rendered.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surface.blit(rendered, rect)


def draw_grid(surface):
    """Menggambar grid tipis sebagai latar belakang."""
    for x in range(0, settings.WINDOW_WIDTH, settings.CELL_SIZE):
        pygame.draw.line(surface, settings.GRAY, (x, 0),
                         (x, settings.WINDOW_HEIGHT))
    for y in range(0, settings.WINDOW_HEIGHT, settings.CELL_SIZE):
        pygame.draw.line(surface, settings.GRAY, (0, y),
                         (settings.WINDOW_WIDTH, y))


def quit_game():
    """Keluar dari game dengan bersih."""
    pygame.quit()
    sys.exit()