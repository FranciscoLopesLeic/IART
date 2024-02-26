import sys
import pygame
from pygame.locals import *
from draw import *
from utils import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))

screen_width, screen_height = screen.get_size()

#Button Start Pos
button_start_width = 400
button_start_height = 100
x_button_start = (screen_width - button_start_width) // 2
y_button_start = ((screen_height - button_start_height) // 2) -50

button_options_width = 400
button_options_height = 100
x_button_options = (screen_width - button_options_width) // 2
y_button_options = ((screen_height - button_options_height) // 2) + 75

button_quit_width = 400
button_quit_height = 100
x_button_quit = (screen_width - button_quit_width) // 2
y_button_quit = ((screen_height - button_quit_height) // 2) + 200

button_start = Button(x_button_start, y_button_start, button_start_width, button_start_height, "Start", (125,0,150),(0,0,0),60)
button_quit = Button(x_button_quit, y_button_quit, button_quit_width, button_quit_height, "Quit", (255, 0, 100), (255, 255, 255), 60)
button_options = Button(x_button_options, y_button_options, button_options_width, button_options_height, "Options", (0, 0, 255), (255, 255, 255), 60)

# Game loop.
while True:
  # Draw Main Menu
  draw_main_menu(screen) 
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
    elif event.type  == MOUSEBUTTONDOWN:
        if button_start.is_clicked(pygame.mouse.get_pos()):
            pygame.quit()
            sys.exit()
        elif button_options.is_clicked(pygame.mouse.get_pos()):
            while True:
                draw_options_menu(screen)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type  == MOUSEBUTTONDOWN:
                        if button_start.is_clicked(pygame.mouse.get_pos()):
                            pygame.quit()
                            sys.exit()
                        elif button_options.is_clicked(pygame.mouse.get_pos()):
                            pygame.quit()
                            sys.exit()
        elif button_quit.is_clicked(pygame.mouse.get_pos()):
                pygame.quit()
                sys.exit()


  # Update.
  
  # Draw.
  button_start.draw(screen)
  button_quit.draw(screen)
  button_options.draw(screen)
  
  pygame.display.flip()
  fpsClock.tick(fps)

