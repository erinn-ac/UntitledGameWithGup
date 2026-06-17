print("hello guppy boy")

import pygame
import Level
import settings
import Player
from pygame.locals import *

pygame.init()

### grid - not currently using this for anything
gridx = int(settings.SCREEN_WIDTH / settings.TILE_SIZE) 
gridy = int(settings.SCREEN_HEIGHT / settings.TILE_SIZE)
grid = [[0]*gridx]*gridy

### character images
chudImg = pygame.image.load('Assets/chud.png')
blueImg = pygame.image.load('Assets/blue.png')
pinkImg = pygame.image.load('Assets/pink.png')

### screen
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption('Untitled')

### objects
level1 = Level.Level([[0], [0], [0], [0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3], [0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 1, 1, 1, 1], [2], [2], [2], [2], [2]], screen)
#the grid inputted for the level is only configured for one tile size, height and width (aka if u change those it'll look weird)
player = Player.Player(100, 250, pinkImg, screen)


###game loop
keepRunning = True

while keepRunning:
    
    level1.draw_grid()
    player.draw()
   

    #checks for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

    pygame.display.update() #updates the display



pygame.quit()