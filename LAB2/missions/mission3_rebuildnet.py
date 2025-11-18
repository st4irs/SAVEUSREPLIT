import pygame
from core.game import Game
from graph.prim import prim_mst
from graph.kruskal import kruskal_mst
from core.visualizer import VisualGraph

class Mission3:
    def __init__(self, window, cheatmode=False):
        self.window = window
        self.game = Game(window)
        self.cheat = cheatmode

        self.weights = [
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0]
        ]

        self.positions = [
            (200, 150), (350, 80), (350, 220),
            (500, 100), (500, 200)
        ]

        self.visual = VisualGraph(self.window, None, self.positions)

    def run(self):
        running = True
        mode = "PRIM"

        while running:
            self.game.clear()
            self.game.draw_title("Misión 3 – RebuildNet", 40)

            subtitle = f"Algoritmo: {mode}"
            if self.cheat:
                subtitle += "  [CHEAT ACTIVADO]"

            self.game.draw_subtitle(subtitle, 100)

            menu = [
                "P: Prim",
                "K: Kruskal",
                "ENTER: ejecutar",
                "ESC: regresar"
            ]

            self.game.draw_menu(menu, 150)
            self.visual.draw_graph()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p: mode = "PRIM"
                    if event.key == pygame.K_k: mode = "KRUSKAL"
                    if event.key == pygame.K_RETURN: self.execute(mode)
                    if event.key == pygame.K_ESCAPE: running = False

            pygame.display.update()

    def execute(self, mode):
        # Aún sin cheats especiales
        if mode == "PRIM":
            mst = prim_mst(self.weights)
        else:
            mst = kruskal_mst(self.weights)

        print("Árbol de expansión mínima:", mst)
