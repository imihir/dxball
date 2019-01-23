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
        self.radius = 50;
        self.centerx = x
        self.centery = y
        self.speed = 5
        self.direction = randrange(-45, 45)
        if randrange(2) == 0:
            self.direction += 180
        pygame.draw.circle(screen,white,(self.centerx,self.centery),10)        
    def show(self):
        pygame.draw.circle(screen,white,(int(self.centerx),int(self.centery)),10)   
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
        a = (self.centerx - b.centerx) 
        b1 = (self.centery - b.centery)
        c = math.sqrt((a*a) + (b1*b1))
        print(c)
        if c<47:
            return True
        return False
    def bounce(self):
        self.direction = (360 - self.direction) %360   
class brick:
    def __init__(self,x,y):
        self.width = 100;
        self.height = 100;
        self.centerx=x;
        self.centery=y;
def play():
    paddlep = paddle(500,450)
    dball = ball(500,250)
    paddlep.show()
    dball.show()
    while True:
        clock.tick()
        screen.fill(black)
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
        if dball.collision_b(paddlep) :  
            dball.bounce()
        paddlep.show()
        pygame.display.update()         
play()