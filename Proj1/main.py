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
y_button_start = ((screen_height - button_start_height) // 2)

button_start = Button(x_button_start, y_button_start, button_start_width, button_start_height, "Start", (125,125,125),(0,0,0),60)


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
  
  # Update.
  
  # Draw.
  button_start.draw(screen)
  
  pygame.display.flip()
  fpsClock.tick(fps)