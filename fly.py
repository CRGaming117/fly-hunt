# CS 172 Homework 4
# Cristobal Cantu   cac554

import pygame
import random
from drawable import Drawable

class Fly(Drawable):
    def __init__(self, x=0, y=0, radius=1, color=(0,0,0)):
        super().__init__(x, y)
        self.__color = color
        self.__radius = radius
        self.__speed = 1
        self.setSpeed(self.__speed)

    def getRadius(self):
        return self.__radius
    def setRadius(self, radius):
        self.__radius=radius

    def getColor(self):
        return self.__color
    def setColor(self, color):
        self.__color=color

    def getSpeed(self):
        return self.__speed
    def setSpeed(self, speed):
        self.__speed = speed
        self.__xSpeed = speed
        self.__ySpeed = speed

    def getXSpeed(self):
        return self.__xSpeed
    def setXSpeed(self, xSpeed):
        self.__xSpeed=xSpeed
    def getYSpeed(self):
        return self.__ySpeed
    def setYSpeed(self, ySpeed):
        self.__ySpeed=ySpeed
        
    def isColliding(self, other):
        # source: pygame documentation
        # https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect
        return self.get_rect().colliderect(other.get_rect())

    def move(self):
        self.setX(self.getX() + self.__xSpeed)
        self.setY(self.getY() + self.__ySpeed)
        self.wallBounce()
    
    def move_randomly(self):
        # pls dont take points off for optimizing code 
        rand=random.randint(-5,5)
        self.setX(self.getX() + rand)
        self.setY(self.getY() + rand)
    
    def move_better(self, decide):
        self.move()
        if decide:
            #print("decision made")
            rand = random.randint(1,8)
            if rand == 1:
                self.UP()
                self.stopX()
            elif rand==2:
                self.UP()
                self.RIGHT()
            elif rand==3:
                self.stopY()
                self.RIGHT()
            elif rand==4:
                self.DOWN()
                self.RIGHT()
            elif rand==5:
                self.DOWN()
                self.stopX()
            elif rand==6:
                self.DOWN()
                self.LEFT()
            elif rand==7:
                self.stopY()
                self.LEFT()
            elif rand==8:
                self.UP()
                self.LEFT()
            else:
                self.stopX()
                self.stopY()
    
    def escape(self,predator,range):
        #print("escaping")
        distX = predator.getX() - self.getX()
        distY = predator.getY() - self.getY()
        if abs(distX) <= range and abs(distY) <= range:
            if distX > 0:
                self.LEFT()
            elif distX < 0:
                self.RIGHT()
            if distY < 0:
                self.UP()
            elif distY > 0:
                self.DOWN()
        
    
    def UP(self):
        self.__ySpeed = -self.__speed
    def DOWN(self):
        self.__ySpeed = self.__speed
    def RIGHT(self):
        self.__xSpeed = self.__speed
    def LEFT(self):
        self.__xSpeed = -self.__speed
    def stopY(self):
        self.__ySpeed = 0
    def stopX(self):
        self.__xSpeed = 0
    
    def wallBounce(self):
        newX = self.getX()+self.__xSpeed
        newY = self.getY()+self.__ySpeed
        surface = pygame.display.get_surface()
        width, height = surface.get_size()
        if newX <= self.__radius or newX >= width-self.__radius:
            self.__xSpeed = -self.__xSpeed
        if newY <= self.__radius or newY >= height-self.__radius:
            self.__ySpeed = -self.__ySpeed
        # out of bounds fix
        if newX < 0:
            self.setX(10)
        elif newX > width:
            self.setX(width-self.__radius-10)
        if newY < 0:
            self.setY(10)
        elif newY > height:
            self.setY(height-self.__radius-10)
        
    
    def draw(self, surface):
        if self.isVisible():
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)
            
    def get_rect(self):
        newX=self.getX()-self.__radius
        newY=self.getY()-self.__radius
        size=self.__radius*2
        return pygame.Rect(newX,newY,size,size)
        