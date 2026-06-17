print("hello guppy boy")

import pygame
import Level
import settings
from pygame.locals import *

pygame.init()

gridx = int(settings.SCREEN_WIDTH / settings.TILE_SIZE)
gridy = int(settings.SCREEN_HEIGHT / settings.TILE_SIZE)

grid = [[0]*gridx]*gridy

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption('Untitled')
screen.fill((125, 219, 239)) #fiils the screen so it has a blue background



chudImg = pygame.image.load('Assets/chud.png')
blueImg = pygame.image.load('Assets/blue.png')
pinkImg = pygame.image.load('Assets/pink.png')

currentChar = blueImg
        

keepRunning = True

level1 = Level.Level([[0], [0], [0], [0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0], [1], [2], [2], [2], [2], [2]], screen)
currentPos = [100, 250]

while keepRunning:
    
    level1.draw_grid()
    screen.blit(pygame.transform.scale(currentChar, (settings.TILE_SIZE, settings.TILE_SIZE)), (currentPos[0], currentPos[1]))

    #checks for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

    pygame.display.update() #updates the display



pygame.quit()