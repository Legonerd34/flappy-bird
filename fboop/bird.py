import random
import readline
import sys
import threading
import time

import pygame
from base import Base
from pygame import mixer
from pygame.locals import *
from scene import Scene

pygame.init()

class Bird(Base):
    def __init__(self, window, x=50, y=256):
        self.x = x
        self.y = y

                

        self.velocity = 0  
        self.acceleration = 0.25  
        self.jump_strength = -5

        self.bird_upflap = pygame.image.load("./flappybird/redbird-upflap.png")
        self.bird_downflap = pygame.image.load("./flappybird/redbird-downflap.png")
        self.bird_midflap = pygame.image.load("./flappybird/redbird-midflap.png")
        self.image = self.bird_upflap 
         

        self.window = window

        
        self.flap_timer = 0
        self.flap_interval = 0.15  
        

    
    def update(self):
        self.velocity += self.acceleration
        self.y += self.velocity
        

        now = pygame.time.get_ticks()
        if now - self.flap_timer > self.flap_interval * 1000:
            self.flap_timer = now
            if self.image == self.bird_upflap:
                self.image = self.bird_midflap
            elif self.image == self.bird_midflap:
                self.image = self.bird_downflap
            else:
                self.image = self.bird_upflap

    def fall(self):
        self.velocity += self.acceleration
        
    def jump(self):
        self.velocity = self.jump_strength
        

    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))

        

    def render(self):
        self.window.blit(self.image, (self.x, self.y))
