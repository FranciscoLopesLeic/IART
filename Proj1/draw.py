import os
import pygame
from pygame.locals import *
from levels import Piece
from utils import Button

def draw_main_menu(screen):
    screen.fill((95, 158, 160))

    # Title - Load, Scale and Position
    directory = os.path.dirname(__file__)
    image_path = os.path.join(directory, 'images', "title.png")
    img = pygame.image.load(image_path)

    img_width, img_height = img.get_size()
    new_width = img_width * 3
    new_height = img_height * 3
    
    scaled_image = pygame.transform.scale(img, (new_width, new_height))
    screen_width, screen_height = screen.get_size()
    image_width, image_height = scaled_image.get_size()

    x = (screen_width - image_width) // 2
    y = ((screen_height - image_height) // 2) - 200
    screen.blit(scaled_image,(x, y))

def draw_level_menu(screen):
    screen.fill((95, 158, 160))
    screen_width, screen_height = screen.get_size()

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"Level",(255,255,255),screen_width/2,70,80)
    write_on_text(screen,"Choose AI search method:",(255,255,255),260,160,50)
    pygame.display.flip()

def draw_level_select_menu(screen):
    screen.fill((95, 158, 160))  # Cor de fundo para o menu de opções

    screen_width, screen_height = screen.get_size()
    

    pygame.draw.rect(screen, (0,0,0), pygame.Rect(30, 30, screen_width-60, screen_height-60))
    write_on_text(screen,"Level Selection",(255,255,255),screen_width/2,70,80)
    pygame.display.flip()

    # To draw the level buttons, as they are 9, lets create a 3x3 grid

def draw_level_button(screen,text,x,y):
    level_button_width = 100
    level_button_height = 100

    level_button = Button(x , y, level_button_width, level_button_height, text, (0, 0, 0), (255, 255, 255), 80)
    level_button.draw(screen)

def draw_options_menu(screen):
    screen.fill((95, 158, 160))  # Cor de fundo para o menu de opções

    # Title - Load, Scale and Position
    directory = os.path.dirname(__file__)
    image_path = os.path.join(directory, 'images', "title.png")
    img = pygame.image.load(image_path)

    img_width, img_height = img.get_size()
    new_width = img_width * 3
    new_height = img_height * 3

    scaled_image = pygame.transform.scale(img, (new_width, new_height))
    screen_width, screen_height = screen.get_size()
    image_width, image_height = scaled_image.get_size()

    x = (screen_width - image_width) // 2
    y = ((screen_height - image_height) // 2) - 200
    screen.blit(scaled_image, (x, y))

    # Adicione outros elementos do menu de opções conforme necessário
    # Exemplo: Botões para ajustar configurações
    draw_option_button(screen, "Controls", 200, 300)
    draw_option_button(screen, "Credits", 200, 425)
    draw_option_button(screen, "Return", 200, 550)


def draw_option_button(screen, text, x, y):
    # Configurações para os botões de opção
    option_button_width = 400
    option_button_height = 100

    option_button = Button(x * 2.2, y, option_button_width, option_button_height, text, (0, 80, 255), (255, 255, 255), 60)
    option_button.draw(screen)


def draw_credits_screen(screen, screen_width):
    screen.fill((95, 158, 160))  # Cor de fundo para a tela de créditos

    # Adicione elementos da tela de créditos
    font = pygame.font.SysFont(None, 55)
    credits_text = [
        "Game Developed by:",
        "Francisco Lopes",
        "João Fernandes",
        "Rui Silveira"
    ]

    # Desenha o texto de créditos na tela
    y = 200
    for line in credits_text:
        text = font.render(line, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width // 2, y))
        screen.blit(text, text_rect)
        y += 60


def write_on_text(screen,text,color,x,y,font_size):
    directory = os.path.dirname(__file__)
    font_path = os.path.join(directory, 'font', "RadiantKingdom-m5LeV.ttf")
    font = pygame.font.SysFont(font_path,font_size)
    text = font.render(text, True, color) 
    text_rect = text.get_rect(center=(x,y))
    screen.blit(text, text_rect)
    
def draw_board(screen, level, screen_width, screen_height,initial_x,initial_y):
    # screen.fill((95, 158, 160))  # Cor de fundo para o tabuleiro

    initial_state = level["initial_state"]
    # Desenha o tabuleiro
    for row in range(len(initial_state)):
        for col in range(len(initial_state[row])):
            x = (col * (screen_width // len(initial_state[row]))+initial_x)
            y = (row * (screen_height // len(initial_state))+initial_y)
            #pygame.draw.rect(screen, (192, 192, 192), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)), 5)

            # Desenha o conteúdo do tabuleiro
            if initial_state[row][col] == Piece.NORMAL:
                # Desenha um círculo para representar uma peça normal
                pygame.draw.rect(screen, (51, 153, 255), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)))


            elif initial_state[row][col] == Piece.SPECIAL:
                # Desenha um círculo para representar uma peça especial
                pygame.draw.rect(screen, (0, 204, 0), (x, y, screen_width // len(initial_state[row]), screen_height // len(initial_state)))

            # Adicione mais condições conforme necessário

    # O restante do seu código permanece inalterado
