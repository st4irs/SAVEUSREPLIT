import pygame
from core.colors import *


class VisualGraph:
    def __init__(self, window, graph, positions):
        self.window = window
        self.graph = graph
        self.positions = positions
        self.font = pygame.font.SysFont("consolas", 22)

    def draw_graph(self, highlight_node=None, highlight_edge=None, visited=None):
        if visited is None:
            visited = set()

        # ---- Dibujar aristas ----
        for u in range(self.graph.n):
            for v in self.graph.adj[u]:
                if u < v:  # evitar duplicados

                    # Color de arista
                    if highlight_edge == (u, v) or highlight_edge == (v, u):
                        color = YELLOW
                    elif u in visited and v in visited:
                        color = GREEN        # arista recorrida
                    else:
                        color = WHITE

                    pygame.draw.line(
                        self.window, color,
                        self.positions[u], self.positions[v], 2
                    )

        # ---- Dibujar nodos ----
        for i, pos in enumerate(self.positions):

            # Nodo actual (jugador está aquí)
            if i == highlight_node:
                pygame.draw.circle(self.window, CYAN, pos, 28)

            # Nodo visitado
            elif i in visited:
                pygame.draw.circle(self.window, (0, 180, 255), pos, 26)

            # Nodo normal
            else:
                pygame.draw.circle(self.window, BLUE, pos, 25)

            # Número del nodo
            label = self.font.render(str(i), True, WHITE)
            self.window.blit(label, (pos[0] - 6, pos[1] - 10))

    # -----------------------------------
    #   Animación simple (no tocado)
    # -----------------------------------
    def animate_path(self, path, delay=500):
        for node in path:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

            self.window.fill(BLACK)
            self.draw_graph(highlight_node=node)
            pygame.display.update()
            pygame.time.delay(delay)
