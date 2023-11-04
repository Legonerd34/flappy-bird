import random
import readline
import sys
import time

import pygame
from pygame import mixer
from pygame.locals import *


class Base():
    x = 0
    y = 400

    

    def __init__(self, window):
        self.image = pygame.image.load("./flappybird/base.png")
        self.window = window
        
    def get_rect(self):
        return self.image.get_rect(topleft=(self.x, self.y))
    

    def render(self):
        self.window.blit(self.image, (self.x, self.y))
