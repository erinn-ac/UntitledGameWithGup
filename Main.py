print("hello guppy boy")

import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600
TILE_SIZE = 50

gridx = int(SCREEN_WIDTH / TILE_SIZE)
gridy = int(SCREEN_HEIGHT / TILE_SIZE)

grid = [[0]*gridx]*gridy

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Untitled')
screen.fill((125, 219, 239)) #fiils the screen so it has a blue background



chudImg = pygame.image.load('Assets/chud.png')
blueImg = pygame.image.load('Assets/blue.png')
pinkImg = pygame.image.load('Assets/pink.png')

currentChar = blueImg

class Level():
    def __init__(self, grid):
        self.grid = grid

    #load images
    grassBlockImg = pygame.image.load('Assets/grass_block.png')
    dirtBlockImg = pygame.image.load('Assets/dirt_block.png')

    def draw_grid(self):
        
        for i in range(0, len(self.grid)):
            if len(self.grid[i]) == 1:
                if self.grid[i][0] == 1:
                    for j in range(0, SCREEN_WIDTH, TILE_SIZE):
                        screen.blit(pygame.transform.scale(self.grassBlockImg, (TILE_SIZE, TILE_SIZE)), (j, i*TILE_SIZE))

                if self.grid[i][0] == 2:
                    for j in range(0, SCREEN_WIDTH, TILE_SIZE):
                        screen.blit(pygame.transform.scale(self.dirtBlockImg, (TILE_SIZE, TILE_SIZE)), (j, i*TILE_SIZE))
            else:

                for j in range(0, len(self.grid[i])):
                    if self.grid[i][j] == 1:
                        screen.blit(pygame.transform.scale(self.grassBlockImg, (TILE_SIZE, TILE_SIZE)), (j * TILE_SIZE, i * TILE_SIZE))
                    elif self.grid[i][j] == 2:
                        screen.blit(pygame.transform.scale(self.dirtBlockImg, (TILE_SIZE, TILE_SIZE)), (j * TILE_SIZE, i * TILE_SIZE))


    

        

keepRunning = True

level1 = Level([[0], [0], [0], [0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], [0], [1], [2], [2], [2], [2], [2]])
currentPos = [100, 250]

while keepRunning:
    
    level1.draw_grid()
    screen.blit(pygame.transform.scale(currentChar, (TILE_SIZE, TILE_SIZE)), (currentPos[0], currentPos[1]))

    #checks for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

    pygame.display.update() #updates the display



pygame.quit()