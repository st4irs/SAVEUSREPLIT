import pygame
from core.game import Game
from graph.dijkstra import dijkstra
from graph.floyd import floyd
from core.visualizer import VisualGraph

class Mission2:
    def __init__(self, window, cheatmode=False):
        self.window = window
        self.game = Game(window)
        self.cheat = cheatmode   # <--- cheatmode guardado

        self.graph = [
            [0, 4, 0, 0, 0, 0],
            [4, 0, 2, 0, 0, 0],
            [0, 2, 0, 3, 0, 0],
            [0, 0, 3, 0, 5, 0],
            [0, 0, 0, 5, 0, 1],
            [0, 0, 0, 0, 1, 0]
        ]

        self.positions = [
            (150, 150), (300, 100), (300, 200),
            (450, 150), (600, 100), (600, 200)
        ]

        self.visual = VisualGraph(self.window, None, self.positions)

    def run(self):
        running = True
        mode = "DIJKSTRA"

        while running:
            self.game.clear()

            subtitle = f"Modo: {mode}"
            if self.cheat:
                subtitle += "  [CHEAT ACTIVADO]"

            self.game.draw_subtitle(subtitle, 100)

            menu = [
                "Presiona D para Dijkstra",
                "Presiona F para Floyd-Warshall",
                "Presiona ENTER para ejecutar",
                "ESC para volver"
            ]

            self.game.draw_menu(menu, 160)
            self.visual.draw_graph()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d: mode = "DIJKSTRA"
                    if event.key == pygame.K_f: mode = "FLOYD"
                    if event.key == pygame.K_RETURN: self.execute(mode)
                    if event.key == pygame.K_ESCAPE: running = False

            pygame.display.update()

    def execute(self, mode):
        # Nada especial aún para cheatmode
        if mode == "DIJKSTRA":
            dist = dijkstra(self.graph, 0)
            print("Dijkstra distancias:", dist)
        else:
            dist = floyd(self.graph)
            print("Floyd-Warshall matriz:", dist)
