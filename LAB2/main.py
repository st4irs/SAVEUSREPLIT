import pygame
from core.game import Game
from missions.mission1_network_tracer import Mission1
from missions.mission2_saferoute import Mission2
from missions.mission3_rebuildnet import Mission3
from missions.mission4_flowcontrol import Mission4
from missions.mission_final_thecore import MissionFinal

pygame.init()

CHEAT_MODE = False

WIDTH, HEIGHT = 900, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CyberQuest – Guardianes de la Red Global")

def main_menu():
    global CHEAT_MODE
    game = Game(window)
    running = True

    cheat_buffer = ""
    SECRET_CODE = "EDD"


    while running:
        game.clear()

        # Títulos del menú
        game.draw_title("CYBERQUEST", y=50)
        game.draw_subtitle("Guardianes de la Red Global", y=120)

        # Opciones del menú
        options = [
            "1. Misión 1 – Network Tracer (BFS/DFS)",
            "2. Misión 2 – SafeRoute (Dijkstra / Floyd)",
            "3. Misión 3 – RebuildNet (Kruskal / Prim)",
            "4. Misión 4 – FlowControl (Max Flow)",
            "5. Misión Final – The Core",
            "ESC – Salir"
        ]

        game.draw_menu(options, start_y=200)

        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                # --- CHEAT MODE INPUT ---
                if event.unicode.isalpha():
                    cheat_buffer += event.unicode.upper()
                    cheat_buffer = cheat_buffer[-10:]  # limitar tamaño

                    if SECRET_CODE in cheat_buffer:
                        CHEAT_MODE = not CHEAT_MODE
                        cheat_buffer = ""

                # --- MISIONES ---
                if event.key == pygame.K_1:
                    Mission1(window, CHEAT_MODE).run()
                if event.key == pygame.K_2:
                    Mission2(window).run()
                if event.key == pygame.K_3:
                    Mission3(window).run()
                if event.key == pygame.K_4:
                    Mission4(window).run()
                if event.key == pygame.K_5:
                    MissionFinal(window).run()

                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main_menu()
