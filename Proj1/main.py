import sys
import pygame
from pygame.locals import *
from draw import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 1280, 800
screen = pygame.display.set_mode((width, height))

# Game loop.
while True:
  # Draw Main Menu
  draw_main_menu(screen) 
  
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  
  # Draw.
  
  pygame.display.flip()
  fpsClock.tick(fps)