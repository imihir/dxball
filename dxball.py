# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 23:00:23 2019

@author: kalem
"""
import math
from random import randrange
import pygame
import pyglet
pygame.init()
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
page_width = 1000
page_height = 500
size = page_width, page_height
screen = pygame.display.set_mode(size)
pygame.display.set_caption("dxBall")
pygame.display.update()
clock = pyglet.clock.Clock()
clock.set_fps_limit(60)
class paddle:
    def __init__(self,x,y):
        self.width = 120
        self.height = 30
        self.centerx=x
        self.centery=y
    def show(self):     
        pygame.draw.rect(screen, white, [self.centerx, self.centery, self.width, self.height])    
    def movel(self):
        if self.centerx>0:    
            self.centerx=self.centerx-10
    def mover(self):
        if self.centerx<870:
            self.centerx=self.centerx+10    
class ball:
    def __init__(self,x,y):
        self.width = 25
        self.height = 25
        self.centerx = x
        self.centery = y
        self.speed = 6
        self.direction = randrange(-45, 45)
        if randrange(2) == 0:
            self.direction += 180
        pygame.draw.rect(screen, white, [self.centerx, self.centery, self.width, self.height])            
    def show(self):
        pygame.draw.rect(screen, white, [self.centerx, self.centery, self.width, self.height])    
    def move(self):
        direction_radians = math.radians(self.direction)
        self.centerx += self.speed * math.cos(direction_radians)
        self.centery -= self.speed * math.sin(direction_radians)
        if self.centerx>page_width or self.centerx<0:
            self.direction = (180 - self.direction) %360
           # self.direction += randrange(-5, 5) 
        if self.centery<0:
            self.direction = (360 - self.direction) %360   
        if self.centery>page_height :
            return 0     
    def collision_b(self,b):
        xt = self.centerx 
        yt = self.centery 
        xb = self.centerx + self.width
        yb = self.centery + self.height
        xtr = b.centerx 
        ytr = b.centery 
        xbr = b.centerx + b.width
        ybr = b.centery + b.height
        return (xt < xbr) and (xtr < xb) and (yt < ybr) and (ytr < yb)      
    def bounce(self):
         self.direction = (360 - self.direction) %360   
class brick:
    def __init__(self,x,y):
        self.width = 70
        self.height = 25
        self.centerx=x
        self.centery=y
        self.exist=True
    def show(self):
        if self.exist:    
            pygame.draw.rect(screen, white, [self.centerx, self.centery, self.width, self.height])    
    def collision(self,b):
        xt = self.centerx 
        yt = self.centery 
        xb = self.centerx + self.width
        yb = self.centery + self.height
        xtr = b.centerx 
        ytr = b.centery 
        xbr = b.centerx + b.width
        ybr = b.centery + b.height
        if (xt < xbr) and (xtr < xb) and (yt < ybr) and (ytr < yb) and self.exist:
            self.exist=False   
            return True
        return False
def play():
    paddlep = paddle(500,450)
    dball = ball(500,10)
    paddlep.show()
    bricks = [];
    score = 0
    for i in range(0,15):
        b = brick((i*73),20)
        bricks.append(b)
    for i in range(0,15):
        b = brick((i*73),50)
        bricks.append(b)    
    dball.show()
    while True:
        clock.tick()
        screen.fill(black)
        for i in bricks:
            i.show()
        scor = dball.move()
        if scor==0:
            break;
        dball.show()
        pygame_events = pygame.event.get()
        keys_pressed = pygame_events  #pygame.event.get(pygame.KEYDOWN)
        # print(keys_pressed)
        for event in keys_pressed:
            print("x")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                paddlep.movel()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                paddlep.mover()
        for i in bricks:
            if i.collision(dball):
                dball.bounce()
                score += 1
        if dball.collision_b(paddlep):
            dball.bounce()
        paddlep.show()
        
        pygame.display.update()    
        print(score)
while True:        
    play()
    