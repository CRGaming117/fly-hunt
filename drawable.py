# CS 172 Homework 4
# Cristobal Cantu   cac554

import pygame
from abc import ABC, abstractmethod

class Drawable(ABC):
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__visible = True
    
    def getX(self):
        return self.__x
    def setX(self, x):
        self.__x = x
        
    def getY(self):
        return self.__y
    def setY(self, y):
        self.__y = y
        
    def getLoc(self):
        return (self.__x, self.__y)
    def setLoc(self, x, y):
        self.__x = x
        self.__y = y
        
    def isVisible(self):
        return self.__visible
    def setVisible(self,visible):
        # why did you even use an if statement in the instructions??? 😭😭😭😭
        self.__visible = bool(visible) 
            
        
        
    @abstractmethod
    def draw(self, surface):
        pass
    
    @abstractmethod
    def get_rect(self,width=0, height=0):
        if self.isVisible():
            return pygame.Rect(self.__position[0], self.__position[1], width, height)