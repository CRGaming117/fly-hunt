# CS 172 Homework 4
# Cristobal Cantu   cac554

import pygame
from drawable import Drawable

class Frog(Drawable):
    def __init__(self, x=0, y=0,size=20, color=(0,255,0)):
        super().__init__(x, y) 
        self.__size = size
        self.__color = color
    
    def getSize(self):
        return self.__size
    def setSize(self, size):
        self.__size=size
    
    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color=color
    
    def hunt(self, fly):
        # right
        if self.getX() < fly.getX():
            self.setX(self.getX()+1)
        # left
        elif self.getX() > fly.getX():
            self.setX(self.getX()-1)
        # down
        if self.getY() < fly.getY():
            self.setY(self.getY()+1)
        # up
        elif self.getY() > fly.getY():
            self.setY(self.getY()-1)
        
    def follow_mouse(self):
        mouseX, mouseY = pygame.mouse.get_pos()
        self.setLoc(mouseX, mouseY)
    
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__size//2)
            
    def get_rect(self):
        return pygame.Rect(self.getX()-(self.__size//2), self.getY()-(self.__size//2), self.__size, self.__size)