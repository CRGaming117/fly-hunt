# CS 172 Homework 4
# Cristobal Cantu   cac554

import pygame
from drawable import Drawable

class Text(Drawable):
    def __init__(self, text="Pygame", x=0, y=0, color=(0,0,0), fontSize=24):
        super().__init__(x, y)
        self.__text = text
        self.__color=color
        self.__font = pygame.font.Font('freesansbold.ttf', fontSize)
        self.__textSurf = self.__font.render(self.__text, True, self.__color)

    def get_rect(self):
        return self.__textSurf.get_rect()

    def draw(self, surface):
        if self.isVisible():
            self.__textSurf = self.__font.render(self.__text, True, self.__color)
            surface.blit(self.__textSurf, self.getLoc())

    def getText(self):
        return self.__text
    def setText(self, text):
        self.__text = text

    def getFont(self):
        return self.__font
    def setFont(self, font):
        self.__font = font

    def getSize(self):
        return self.__font.size(self.__text)
    def setSize(self, size):
        self.__font = pygame.font.Font('freesansbold.ttf', size)
    
