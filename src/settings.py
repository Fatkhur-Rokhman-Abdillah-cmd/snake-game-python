"""Konfigurasi global untuk game Snake."""

# Ukuran layar
WINDOW_WIDTH = 720
WINDOW_HEIGHT = 480
FPS = 10

# Ukuran grid
CELL_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // CELL_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // CELL_SIZE

# Warna (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 120, 0)
RED = (220, 20, 60)
GRAY = (40, 40, 40)

# Judul window
WINDOW_TITLE = "Snake Classic - Pygame"

# Kecepatan awal
INITIAL_SPEED = 8
SPEED_INCREMENT = 0.5