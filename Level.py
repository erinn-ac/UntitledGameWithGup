import pygame
from pygame.locals import *
import settings


class Level():
    def __init__(self, grid, screen):
        self.grid = grid
        self.screen = screen

    #load images
    grassBlockImg = pygame.image.load('Assets/grass_block.png')
    dirtBlockImg = pygame.image.load('Assets/dirt_block.png')

    def draw_grid(self):
        
        for i in range(0, len(self.grid)):
            if len(self.grid[i]) == 1:
                if self.grid[i][0] == 1:
                    for j in range(0, settings.SCREEN_WIDTH, settings.TILE_SIZE):
                        self.screen.blit(pygame.transform.scale(self.grassBlockImg, (settings.TILE_SIZE, settings.TILE_SIZE)), (j, i*settings.TILE_SIZE))

                if self.grid[i][0] == 2:
                    for j in range(0, settings.SCREEN_WIDTH, settings.TILE_SIZE):
                        self.screen.blit(pygame.transform.scale(self.dirtBlockImg, (settings.TILE_SIZE, settings.TILE_SIZE)), (j, i*settings.TILE_SIZE))
            else:

                for j in range(0, len(self.grid[i])):
                    if self.grid[i][j] == 1:
                        self.screen.blit(pygame.transform.scale(self.grassBlockImg, (settings.TILE_SIZE, settings.TILE_SIZE)), (j * settings.TILE_SIZE, i * settings.TILE_SIZE))
                    elif self.grid[i][j] == 2:
                        self.screen.blit(pygame.transform.scale(self.dirtBlockImg, (settings.TILE_SIZE, settings.TILE_SIZE)), (j * settings.TILE_SIZE, i * settings.TILE_SIZE))