print("hello guppy boy")

import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 600

gridx = int(SCREEN_WIDTH / 50)
gridy = int(SCREEN_HEIGHT / 50)

grid = [[0]*gridx]*gridy

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Untitled')
screen.fill((125, 219, 239)) #fiils the screen so it has a blue background

### loading images
grassBlockImg = pygame.image.load('Assets/grass_block.png')
dirtBlockImg = pygame.image.load('Assets/dirt_block.png')

chudImg = pygame.image.load('Assets/chud.png')

def draw_screen(start_y, start_x):
    
    block_dim = 50 #if 50, a block is 50 x 50 pixels

    #draws row of grass blocks across screen
    for i in range(0, SCREEN_WIDTH, block_dim):
        screen.blit(pygame.transform.scale(grassBlockImg, (block_dim, block_dim)), (i, start_y))

    #draws row of dirt blocks across screen for every 'row' under grass block row
    for i in range(start_y + block_dim, SCREEN_HEIGHT, block_dim):
        for j in range(0, SCREEN_WIDTH, block_dim):
            screen.blit(pygame.transform.scale(dirtBlockImg, (block_dim, block_dim)), (j, i))



    screen.blit(pygame.transform.scale(chudImg, (50, 50)), (100, 300))



keepRunning = True

while keepRunning:
    
    draw_screen(350, 50)

    

    #checks for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keepRunning = False

    pygame.display.update() #updates the display



pygame.quit()