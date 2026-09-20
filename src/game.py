"""Logika utama game Snake."""

import pygame
from src import settings
from src.snake import Snake
from src.food import Food
from src.utils import draw_text, draw_grid


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(
            (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
        )
        pygame.display.set_caption(settings.WINDOW_TITLE)
        self.clock = pygame.time.Clock()
        self.running = True
        self.reset()

    def reset(self):
        """Reset state game."""
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.score = 0
        self.speed = settings.INITIAL_SPEED
        self.game_over = False
        self.paused = False

    def handle_events(self):
        """Tangani input dari user."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                # Kontrol arah
                if event.key in (pygame.K_UP, pygame.K_w):
                    self.snake.change_direction((0, -1))
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    self.snake.change_direction((0, 1))
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    self.snake.change_direction((-1, 0))
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    self.snake.change_direction((1, 0))

                # Pause
                if event.key == pygame.K_p and not self.game_over:
                    self.paused = not self.paused

                # Restart
                if event.key == pygame.K_r:
                    self.reset()

                # Keluar
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        """Update logika game."""
        if self.paused or self.game_over:
            return

        alive = self.snake.move()
        if not alive:
            self.game_over = True
            return

        # Cek makan
        if self.snake.get_head() == self.food.position:
            self.snake.grow()
            self.score += 10
            self.speed += settings.SPEED_INCREMENT
            self.food.randomize(self.snake.body)

    def draw(self):
        """Gambar semua elemen."""
        self.screen.fill(settings.BLACK)
        draw_grid(self.screen)
        self.food.draw(self.screen)
        self.snake.draw(self.screen)

        # Skor
        draw_text(self.screen, f"Score: {self.score}", 24,
                  settings.WHITE, 10, 10)

        # Overlay pause
        if self.paused:
            draw_text(self.screen, "PAUSED", 60, settings.WHITE,
                      settings.WINDOW_WIDTH // 2,
                      settings.WINDOW_HEIGHT // 2, center=True)
            draw_text(self.screen, "Tekan P untuk lanjut", 20,
                      settings.WHITE,
                      settings.WINDOW_WIDTH // 2,
                      settings.WINDOW_HEIGHT // 2 + 50, center=True)

        # Overlay game over
        if self.game_over:
            overlay = pygame.Surface(
                (settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT)
            )
            overlay.set_alpha(180)
            overlay.fill(settings.BLACK)
            self.screen.blit(overlay, (0, 0))
            draw_text(self.screen, "GAME OVER", 64, settings.RED,
                      settings.WINDOW_WIDTH // 2,
                      settings.WINDOW_HEIGHT // 2 - 40, center=True)
            draw_text(self.screen, f"Skor Akhir: {self.score}", 28,
                      settings.WHITE,
                      settings.WINDOW_WIDTH // 2,
                      settings.WINDOW_HEIGHT // 2 + 20, center=True)
            draw_text(self.screen, "Tekan R untuk main lagi / ESC keluar",
                      18, settings.WHITE,
                      settings.WINDOW_WIDTH // 2,
                      settings.WINDOW_HEIGHT // 2 + 70, center=True)

        pygame.display.flip()

    def run(self):
        """Loop utama game."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.speed)

        pygame.quit()