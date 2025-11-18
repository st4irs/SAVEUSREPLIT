import pygame, time, random
from core.game import Game
from graph.graph import Graph
from graph.bfs import bfs
from graph.dfs import dfs
from core.visualizer import VisualGraph


class Mission1:
    def __init__(self, window, cheat_mode=False):
        self.window = window
        self.cheat_mode = cheat_mode

        self.game = Game(window)
        self.font = pygame.font.SysFont("consolas", 22)

        # Nombres de servidores
        self.server_names = [
            "Firewall Central", "Correo", "Base de Datos",
            "Proxy", "DNS", "Nodo Infectado"
        ]

        # Visual positions
        self.positions = [
            (150, 150), (350, 100), (350, 200),
            (550, 100), (550, 200), (750, 150)
        ]

    # -----------------------------------
    #    GENERAR ÁRBOL ALEATORIO
    # -----------------------------------
    def generate_random_tree(self, n):
        tree = Graph(n)
        for node in range(1, n):
            parent = random.randint(0, node - 1)
            tree.add_edge(parent, node)
        return tree

    # -----------------------------------
    #          MENÚ DE LA MISIÓN
    # -----------------------------------
    def run(self):

        # Reiniciar vidas y tiempo cada partida
        self.lives = 1000 if self.cheat_mode else 5
        self.time_limit = 1000 if self.cheat_mode else 25

        # Generar árbol nuevo
        self.graph = self.generate_random_tree(6)

        # Crear visualizador
        self.visual = VisualGraph(self.window, self.graph, self.positions)

        mode = "BFS"
        running = True

        while running:
            self.game.clear()

            self.game.draw_title("Misión 1 – Network Tracer", 40)
            self.game.draw_subtitle(f"Modo actual: {mode}", 100)

            instructions = [
                "B: Usar BFS",
                "D: Usar DFS",
                "ENTER: Comenzar misión",
                "ESC: Volver al menú"
            ]
            self.game.draw_menu(instructions, 150)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_b: mode = "BFS"
                    if event.key == pygame.K_d: mode = "DFS"
                    if event.key == pygame.K_RETURN:
                        self.interactive_play(mode)
                    if event.key == pygame.K_ESCAPE:
                        running = False

            pygame.display.update()

    # -----------------------------------
    #      GAMEPLAY INTERACTIVO REAL
    # -----------------------------------
    def interactive_play(self, mode):

        # Secuencia correcta
        solution = bfs(self.graph, 0) if mode == "BFS" else dfs(self.graph, 0)

        # Ruta real del jugador
        player_path = [solution[0]]

        # NUEVO → Nodos visitados
        visited_nodes = set()
        visited_nodes.add(solution[0])

        step = 0
        total_steps = len(solution) - 1

        running = True

        while running:
            current = solution[step]
            neighbors = self.graph.adj[current]

            start_time = time.time()

            while True:
                elapsed = time.time() - start_time
                remaining = max(0, int(self.time_limit - elapsed))

                if remaining == 0:
                    return self.fail_and_restart("¡Se acabó el tiempo!")

                # Render
                self.window.fill((0, 0, 0))
                self.visual.draw_graph(
                    highlight_node=current,
                    visited=visited_nodes        # ← NUEVO
                )

                self.window.blit(self.font.render(
                    f"Vidas: {self.lives}", True, (255, 50, 50)), (30, 20))

                self.window.blit(self.font.render(
                    f"Tiempo restante: {remaining}s",
                    True, (255, 255, 0)), (30, 60))

                self.window.blit(self.font.render(
                    f"Estás en: {self.server_names[current]}",
                    True, (0, 255, 255)), (30, 420))

                txt = ", ".join([f"{n}" for n in neighbors])
                self.window.blit(self.font.render(
                    f"Nodos posibles: {txt}",
                    True, (0, 255, 0)), (30, 460))

                if self.cheat_mode:
                    cheat = f"CHEAT: {mode} path = {solution}"
                    self.window.blit(self.font.render(cheat, True, (255, 255, 0)), (20, 520))

                pygame.display.update()

                # Input
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return

                    if event.type == pygame.KEYDOWN:
                        if pygame.K_0 <= event.key <= pygame.K_9:

                            choice = event.key - pygame.K_0

                            expected = solution[step + 1] if step + 1 <= total_steps else None

                            player_path.append(choice)

                            # ERROR
                            if choice != expected:
                                player_path.pop()
                                self.lives -= 1

                                if self.lives == 0:
                                    return self.fail_and_restart("Sin vidas restantes.")

                                self.show_error("Ese no es el nodo correcto.")
                                continue

                            # CORRECTO → avanzar
                            step += 1
                            visited_nodes.add(solution[step])   # ← NUEVO

                            if step == total_steps:
                                if player_path[1:] == solution[1:]:
                                    return self.success_message()
                                else:
                                    return self.fail_and_restart("La ruta no coincide.")

                            break

    # -----------------------------------
    #        MENSAJES DEL GANE / FAIL
    # -----------------------------------
    def fail_and_restart(self, cause):
        self.window.fill((0, 0, 0))
        self.game.draw_title("Fallaste", 40)
        self.game.draw_subtitle(cause, 150)
        self.game.draw_subtitle("Reiniciando misión...", 250)
        pygame.display.update()
        pygame.time.delay(1500)
        return self.run()

    def show_error(self, text):
        self.window.fill((20, 0, 0))
        self.game.draw_title("Error", 40)
        self.game.draw_subtitle(text, 150)
        pygame.display.update()
        pygame.time.delay(1200)

    def success_message(self):
        running = True
        while running:
            self.game.clear()
            self.game.draw_title("¡Rastreo completado!", 40)
            self.game.draw_subtitle("Has localizado el nodo raíz del virus.", 150)
            self.game.draw_subtitle("Código desbloqueado: CYB3R-KEY-001", 220)
            self.game.draw_subtitle("Pulsa ESC para volver al menú", 300)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            pygame.display.update()
