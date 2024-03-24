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
    
class CheckBox:

    def __init__(self,x,y,width,height,checkbox_color,color_select,color_unselect,border_width):
        # Useful to draw if see it is clicked!
        self.rectangle=pygame.Rect(x+(border_width/2),y+(border_width/2),width-(border_width),height-(border_width))

        self.x= x
        self.y = y
        self.width = width
        self.height = height
        self.checkbox_color = checkbox_color
        self.color_select = color_select
        self.color_unselect = color_unselect
        self.border_width = border_width
        self.selected = False

    def draw(self,screen):
        # Draw top border
        pygame.draw.line(screen, self.checkbox_color, (self.x, self.y), (self.x + self.width, self.y), self.border_width)
        # Draw bottom border
        pygame.draw.line(screen, self.checkbox_color, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), self.border_width)
        # Draw left border
        pygame.draw.line(screen, self.checkbox_color, (self.x, self.y), (self.x, self.y + self.height), self.border_width)
        # Draw right border
        pygame.draw.line(screen, self.checkbox_color, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), self.border_width)
        pygame.display.flip()
    def is_clicked(self, screen, pos):
        if self.rectangle.collidepoint(pos) and self.selected:
            pygame.draw.rect(screen,self.color_unselect,self.rectangle)
            self.selected = False
            pygame.display.flip()
            return True
        elif self.rectangle.collidepoint(pos) and (not self.selected):
            self.selected = True
            pygame.draw.rect(screen,self.color_select,self.rectangle)
            pygame.display.flip()
            return True
        else:
            return False,



