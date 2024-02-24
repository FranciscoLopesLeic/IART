import pygame
from pygame.locals import *

class Button:

    def __init__(self,x,y,width,height,text,button_color,text_color,font_size):
        self.rectangle=pygame.Rect(x,y,width,height)
        self.text = text
        self.button_color=button_color
        self.text_color = text_color
        self.font_size = font_size

    def draw(self,screen):
        pygame.draw.rect(screen,self.button_color,self.rectangle)