# CS 172 Homework 4
# Cristobal Cantu   cac554
# MAIN CLASS
import pygame
import random
from fly import Fly
from frog import Frog
from text import Text

pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fly Hunt')
BLACK = (0, 0, 0)
PINK = (255, 100, 200)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
DARKBLUE = (0, 0, 100)

numEaten = 0
winNum = 0

flies = []
for i in range(20):
    flies.append(Fly(random.randint(20,surface.get_width()-20),random.randint(20,surface.get_height()-20), 10, BLACK))
    winNum+=1
    flies[i].setSpeed(2)
blueflies = []
for i in range(5):
    blueflies.append(Fly(random.randint(20,surface.get_width()-20),random.randint(20,surface.get_height()-20), 8, DARKBLUE))
    winNum+=2
    blueflies[i].setSpeed(5)
flies.extend(blueflies)
ladybugs = []
for i in range(3):
    ladybugs.append(Fly(random.randint(20,surface.get_width()-20),random.randint(20,surface.get_height()-20), 12, RED))
flies.extend(ladybugs)

frog1 = Frog(400, 300,30,PINK)
frog1.setVisible(False)
scoreBoard = Text("Score: 0", 10, 10)
winMsg = Text("You won!",0,0,GREEN,100)
winMsg.setLoc((surface.get_width()//2)-(winMsg.get_rect().width//2), (surface.get_height()//2)-(winMsg.get_rect().height//2))
winMsg.setVisible(False)
loseMsg = Text("You lost.",0,0,RED,100)
loseMsg.setLoc((surface.get_width()//2)-(winMsg.get_rect().width//2), (surface.get_height()//2)-(winMsg.get_rect().height//2))
loseMsg.setVisible(False)

running = True
fpsClock = pygame.time.Clock()
while running:
    surface.fill((0,0,255))
    
    for fly in flies:
        if winMsg.isVisible() or loseMsg.isVisible():
            fly.setVisible(False)
        
        if (not loseMsg.isVisible()) or (not winMsg.isVisible()):
            fly.draw(surface)
            if fly.getColor()==RED and fly.isVisible():
                s=4
                #pygame.draw.rect(surface, RED, fly.get_rect(),2)
                pygame.draw.circle(surface,BLACK,fly.getLoc(),s)
                if fly.getXSpeed()==0 or fly.getYSpeed()==0:
                    d=6
                    pygame.draw.circle(surface,BLACK,(fly.getX()-d,fly.getY()-d),s)
                    pygame.draw.circle(surface,BLACK,(fly.getX()+d,fly.getY()-d),s)
                    pygame.draw.circle(surface,BLACK,(fly.getX()-d,fly.getY()+d),s)
                    pygame.draw.circle(surface,BLACK,(fly.getX()+d,fly.getY()+d),s)
                else:
                    d=9
                    pygame.draw.circle(surface,BLACK,(fly.getX(),fly.getY()-d),s)
                    pygame.draw.circle(surface,BLACK,(fly.getX()+d,fly.getY()),s)
                    pygame.draw.circle(surface,BLACK,(fly.getX(),fly.getY()+d),s)
                    pygame.draw.circle(surface,BLACK,(fly.getX()-d,fly.getY()),s)
            
        fly.move_better(fpsClock.get_time()>=35)
        if fly.getColor()== DARKBLUE:
            #print(fly.getLoc())
            fly.escape(frog1,50)
            
        if fly.isVisible() and frog1.isVisible() and fly.isColliding(frog1):
            fly.setVisible(False)
            print("fly caught")
            if fly.getColor() == BLACK:
                numEaten += 1
            elif fly.getColor() == DARKBLUE:
                numEaten += 2
            elif fly.getColor() == RED:
                loseMsg.setVisible(True)
            scoreBoard.setText("Score: " + str(numEaten))
    
    frog1.draw(surface)
    #pygame.draw.rect(surface, RED, frog1.get_rect(),2)
    frog1.follow_mouse()

    # scope
    if not frog1.isVisible():
        pygame.draw.circle(surface, PINK, frog1.getLoc(),frog1.getSize()//2,2)
        pygame.draw.line(surface,PINK,(frog1.getX(),frog1.getY()-frog1.getSize()),(frog1.getX(),frog1.getY()+frog1.getSize()),2)
        pygame.draw.line(surface,PINK,(frog1.getX()-frog1.getSize(),frog1.getY()),(frog1.getX()+frog1.getSize(),frog1.getY()),2)
    else:
        pygame.draw.line(surface,PINK,(frog1.getX(),frog1.getY()),(surface.get_width()//2,surface.get_height()),frog1.getSize()-5)
    #frog
    povSize = 100
    pygame.draw.circle(surface,GREEN,((surface.get_width()//2)-(povSize//2),surface.get_height()-int(povSize*.75)),int((povSize//2.5)))
    pygame.draw.circle(surface,GREEN,((surface.get_width()//2)+(povSize//2),surface.get_height()-int(povSize*.75)),int((povSize//2.5)))
    pygame.draw.circle(surface,GREEN,(surface.get_width()//2,surface.get_height()),povSize)
    
    scoreBoard.draw(surface)
    
    winMsg.setVisible(numEaten == winNum)
    winMsg.draw(surface)
    loseMsg.draw(surface)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            frog1.setVisible(True)
        elif event.type == pygame.MOUSEBUTTONUP:
            frog1.setVisible(False)

    pygame.display.update()
    fpsClock.tick(30) # 30 fps
exit()