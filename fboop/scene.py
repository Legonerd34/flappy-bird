import random
import readline
import sys
import time

import pygame
from pygame import mixer
from pygame.locals import *


class Scene():
    x = 0
    y = 0

    def __init__(self, window):
        self.background = pygame.image.load("./flappybird/background-night.png")
        self.window = window
    
    def render(self):
        self.window.blit(self.background, (0,0))