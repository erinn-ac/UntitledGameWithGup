import pygame
import settings

class Player:
    def __init__(self, x, y, img, screen): 
        self.img = pygame.transform.scale(img, (settings.TILE_SIZE, settings.TILE_SIZE))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.screen = screen

    def draw(self):
        self.screen.blit(self.img, self.rect)

    def update_position(self, new_x, new_y):
        self.rect.x = new_x
        self.rect.y = new_y

    