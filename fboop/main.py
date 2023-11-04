import random
import readline
import sys
import threading
import time
from pipes import Pipes

import pygame
from base import Base
from bird import Bird
from pygame import mixer
from pygame.locals import *
from scene import Scene

pygame.init()

height = 512
width = 288

clock = pygame.time.Clock()

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")
mixer.music.set_volume(1)

scene = Scene(window)
base = Base(window)
pipes = Pipes(window)
bird = Bird(window)

def main():

    
    highScore = "0"
    
    bigFont = pygame.font.SysFont("Helvetica neue", 40)
    font = pygame.font.SysFont("Helvetica neue", 15)

    
    lightGreen = (153, 255, 204)
    black = (0, 0, 0)

    youLose = bigFont.render("You Lose!",     True, lightGreen)
    playAgain = bigFont.render("Play Again?", True, lightGreen)

    score = font.render("Your score was: " + highScore, True, black)

    running = True
    hit_count = 0
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

            
        pipes.move()
        bird.update()

        bird.fall()

        bird_rect = bird.get_rect()
        base_rect = base.get_rect()
        pipe1 = pipes.get_rect_bottom()
        pipe2 = pipes.get_rect_top()

        

        if bird_rect.colliderect(pipe1) or bird_rect.colliderect(pipe2):
            hit_count += 1
            print(hit_count)

        if bird_rect.colliderect(base_rect):
            hit_count += 1
            print(hit_count)

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN:
                bird.jump()
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('fboop/flappybird/flap.mp3'))

        scene.render()
        base.render()

        pipes.render()
        bird.render()

        pygame.display.update()

        if int(hit_count) >= 1:
            highScore = pipes.get_highScore()
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('fboop/flappybird/Roblox-death-sound.mp3'))
            window.blit(youLose,(10,200))
            window.blit(playAgain,(10,300))
            window.blit(score, (10, 350))
            pygame.display.update()
            clock.tick(60)

            time.sleep(3)

            running = False
            

        clock.tick(60)
        pygame.display.update()

if __name__ == "__main__":
    main()

sys.exit()