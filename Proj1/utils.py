import os
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
        directory = os.path.dirname(__file__)
        font_path = os.path.join(directory, 'font', "RadiantKingdom-m5LeV.ttf")
        font = pygame.font.SysFont(font_path,self.font_size)
        text = font.render(self.text, True, self.text_color) 
        text_rect = text.get_rect(center=self.rectangle.center)
        screen.blit(text, text_rect)
    
    def is_clicked(self, pos):
        return self.rectangle.collidepoint(pos)


