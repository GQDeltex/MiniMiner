import pygame
import constants

class Wall(object):
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.rect.y = y
        self.rect.x = x

class Wall_tiles(object):
    def __init__(self, x, y):
        self.rect = pygame.Rect((x*32), (y*32), 32, 32)
        self.rect.x = (x*32)
        self.rect.y = (y*32)