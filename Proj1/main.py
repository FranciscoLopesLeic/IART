import sys
import pygame
from pygame.locals import *
from draw import *
from utils import *
from levels import beginner_1
from typing import Dict, List
from game import Game

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 800
screen = pygame.display.set_mode((width, height))

screen_width, screen_height = screen.get_size()

class GameState:
    MAIN_MENU = "main_menu"
    OPTIONS_MENU = "options_menu"
    CREDITS_SCREEN = "credits_screen"
    PLAYING = "Interface"

current_state = GameState.MAIN_MENU

# Variáveis para o menu principal
button_start_width = 400
button_start_height = 100
x_button_start = (screen_width - button_start_width) // 2
y_button_start = ((screen_height - button_start_height) // 2) - 50

button_options_width = 400
button_options_height = 100
x_button_options = (screen_width - button_options_width) // 2
y_button_options = ((screen_height - button_options_height) // 2) + 75

button_quit_width = 400
button_quit_height = 100
x_button_quit = (screen_width - button_quit_width) // 2
y_button_quit = ((screen_height - button_quit_height) // 2) + 200

button_start = Button(x_button_start, y_button_start, button_start_width, button_start_height, "Start", (125, 0, 150), (0, 0, 0), 60)
button_options = Button(x_button_options, y_button_options, button_options_width, button_options_height, "Options", (0, 80, 255), (255, 255, 255), 60)
button_quit = Button(x_button_quit, y_button_quit, button_quit_width, button_quit_height, "Quit", (255, 40, 100), (255, 255, 255), 60)

# Variáveis para o menu de opções
button_controls_width = 400
button_controls_height = 100
x_button_controls = (screen_width - button_controls_width) // 2
y_button_controls = ((screen_height - button_controls_height) // 2) - 50

button_credits_width = 400
button_credits_height = 100
x_button_credits = (screen_width - button_credits_width) // 2
y_button_credits = ((screen_height - button_credits_height) // 2) + 75

button_return_width = 400
button_return_height = 100
x_button_return = (screen_width - button_return_width) // 2
y_button_return = ((screen_height - button_return_height) // 2) + 200

button_controls = Button(x_button_controls, y_button_controls, button_controls_width, button_controls_height, "Controls", (0, 80, 255), (0, 0, 0), 60)
button_credits = Button(x_button_credits, y_button_credits, button_credits_width, button_credits_height, "Credits", (0, 80, 255), (255, 255, 255), 60)
button_return = Button(x_button_return, y_button_return, button_return_width, button_return_height, "Return", (0, 80, 255), (255, 255, 255), 60)
draw_main_menu(screen)
while True:
    # Draw Main Menu
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:   
            if button_start.is_clicked(pygame.mouse.get_pos()):
                current_state = GameState.PLAYING
                """if current_state == GameState.PLAYING:
                    # Lógica do jogo
                    # Você pode usar level_1["initial_state"] e level_1["objective_state"] para configurar o estado inicial e objetivo do nível

                    # Exemplo:
                    current_level: Dict[str, List[List[str]]] = beginner_1  # Escolha o nível atual
                    initial_state = current_level["initial_state"]
                    objective_state = current_level["objective_state"]
                    game = Game(initial_state, objective_state)
                    game.run(screen, screen_width, screen_height)"""

            elif button_options.is_clicked(pygame.mouse.get_pos()):
                current_state = GameState.OPTIONS_MENU
            elif button_credits.is_clicked(pygame.mouse.get_pos()):
                current_state = GameState.CREDITS_SCREEN
            elif button_quit.is_clicked(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()

    if current_state == GameState.OPTIONS_MENU:
        draw_options_menu(screen)

    elif current_state == GameState.CREDITS_SCREEN:
        draw_credits_screen(screen, screen_width)
        
    elif current_state == GameState.PLAYING:
        draw_level_select_menu(screen)

    elif current_state == GameState.MAIN_MENU:
        draw_main_menu(screen)
        button_start.draw(screen)
        button_quit.draw(screen)
        button_options.draw(screen)
        # Voltar para o menu principal ao clicar na tela de créditos

    pygame.display.flip()
    fpsClock.tick(fps)