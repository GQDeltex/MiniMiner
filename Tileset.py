import pygame
from Utils import SpriteSheet
import TileType

class Tileset(object):
    def __init__(self, image, tile_width, tile_height):
        self.sprite_sheet = SpriteSheet(image)
        self.image = self.sprite_sheet.getImage (0, 0, 640, 400)
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.tile_types = dict()
    
    def add_tile(self, name, start_x, start_y):
        self.tile_types[name] = TileType.TileType(name, start_x, start_y, self.tile_width, self.tile_height)
    
    def get_tile(self, name):
        try:
            return self.tile_types[name]
        except KeyError:
            return None
        