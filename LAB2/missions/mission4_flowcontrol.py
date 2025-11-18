import pygame
from core.game import Game
from graph.maxflow import edmonds_karp

class Mission4:
    def __init__(self, window, cheatmode=False):
        self.window = window
        self.game = Game(window)
        self.cheat = cheatmode

        self.capacity = [
            [0, 10, 10, 0, 0, 0],
            [0, 0, 2, 4, 8, 0],
            [0, 0, 0, 0, 9, 0],
            [0, 0, 0, 0, 0, 10],
            [0, 0, 0, 6, 0, 10],
            [0, 0, 0, 0, 0, 0]
        ]

    def run(self):
        running = True

        while running:
            self.game.clear()
            title = "Misión 4 – FlowControl"
            if self.cheat:
                title += "  [CHEAT ACTIVADO]"

            self.game.draw_title(title, 40)

            menu = [
                "ENTER: ejecutar flujo máximo",
                "ESC: regresar"
            ]

            self.game.draw_menu(menu, 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        flow = edmonds_karp(self.capacity, 0, 5)
                        print("Flujo máximo:", flow)

                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
