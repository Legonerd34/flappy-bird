import random
import readline
import sys
import threading
import time

import pygame
from base import Base
from bird import Bird
from pygame import mixer
from pygame.locals import *
from scene import Scene

pygame.init()

class Pipes:

    highScore = "0"
    
    
    

    

    def __init__(self, window, width=288):
        self.x = 200
        self.y1 = random.randint(210, 400)
        self.y2 = random.randint(-300, -120)
        self.speed = 2.5
        self.width = width

        self.top_pipe = pygame.image.load("fboop/flappybird/pipe-green-top.png")
        self.bottom_pipe = pygame.image.load("fboop/flappybird/pipe-green-bottom.png")
        
        self.window = window

        self.bottom_pipe_rect = self.bottom_pipe.get_rect(topleft=(self.x, self.y1))
        self.top_pipe_rect = self.top_pipe.get_rect(topleft=(self.x, self.y2))

    def move(self):
        self.x -= self.speed

        if self.x + self.bottom_pipe.get_width() < 0 or self.x + self.top_pipe.get_width() < 0:
            

            self.x = self.width
            self.y2 = random.randint(-300, -125)
            self.y1 = random.randint(210, 395)
            self.speed += 0.05
            self.highScore = int(self.highScore)
            self.highScore += 1
            self.highScore = str(self.highScore)
            print(self.highScore)
            pygame.mixer.Channel(2).play(pygame.mixer.Sound('fboop/flappybird/point.mp3'))
            
            

    def get_rect_top(self):
        return self.top_pipe.get_rect(topleft=(self.x, self.y2))

    def get_rect_bottom(self):
        return self.bottom_pipe.get_rect(topleft=(self.x, self.y1))

    def get_highScore(self):
        self.highscore = str(self.highScore)
        return self.highScore

    def render(self):
        self.window.blit(self.bottom_pipe, (self.x, self.y1))
        self.window.blit(self.top_pipe, (self.x, self.y2))
        



        

