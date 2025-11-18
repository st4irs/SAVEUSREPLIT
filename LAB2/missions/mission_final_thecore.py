import pygame
from core.game import Game
from graph.bfs import bfs
from graph.dijkstra import dijkstra
from graph.prim import prim_mst
from graph.maxflow import edmonds_karp

class MissionFinal:
    def __init__(self, window, cheatmode=False):
        self.window = window
        self.game = Game(window)
        self.cheat = cheatmode

    def run(self):
        running = True

        while running:
            self.game.clear()

            title = "Misión Final – THE CORE"
            if self.cheat:
                title += "  [CHEAT ACTIVADO]"

            self.game.draw_title(title, 40)
            self.game.draw_subtitle("Completa los 4 algoritmos en secuencia", 100)

            menu = [
                "ENTER: Resolver todo automáticamente",
                "ESC: regresar"
            ]

            self.game.draw_menu(menu, 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        print("\n--- INICIANDO SECUENCIA FINAL ---")
                        print("BFS:", bfs({0:[1],1:[2],2:[]}, 0))
                        print("Dijkstra:", dijkstra([[0,2],[2,0]], 0))
                        print("Prim:", prim_mst([[0,1],[1,0]]))
                        print("Maxflow:", edmonds_karp([[0,5],[0,0]], 0, 1))
                        print("VICTORIA TOTAL – NEMESIS ELIMINADO")

                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()
