import os
import pygame
from pygame.locals import *

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
    screen.blit(scaled_image,(x,y))


def draw_options_menu(screen):
    screen.fill((173, 216, 230))  # Cor de fundo para o menu de opções

    # Title - Load, Scale and Position
    directory = os.path.dirname(__file__)
    image_path = os.path.join(directory, 'images', "options_title.png")
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
    draw_option_button(screen, "Volume", 200, 300)
    draw_option_button(screen, "Controls", 200, 400)

def draw_option_button(screen, text, x, y):
    # Configurações para os botões de opção
    option_button_width = 400
    option_button_height = 100

    option_button = Button(x, y, option_button_width, option_button_height, text, (255, 0, 100), (255, 255, 255), 40)
    option_button.draw(screen)
