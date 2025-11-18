import pygame
from core.colors import *

class Game:
    def __init__(self, window):
        self.window = window
        self.font = pygame.font.SysFont("consolas", 28)
        self.small_font = pygame.font.SysFont("consolas", 20)

    def clear(self):
        self.window.fill(BLACK)

    def draw_title(self, text, y):
        surface = self.font.render(text, True, CYAN)
        self.window.blit(surface, (50, y))

    def draw_subtitle(self, text, y):
        surface = self.small_font.render(text, True, GREEN)
        self.window.blit(surface, (50, y))

    def draw_menu(self, options, start_y):
        y = start_y
        for option in options:
            surface = self.small_font.render(option, True, WHITE)
            self.window.blit(surface, (50, y))
            y += 40
