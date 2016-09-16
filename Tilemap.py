import pygame
import Tileset
import wall_tools

class Tilemap(object):
    def __init__(self, walls):
        self.tiles = list()
        
        self.tileset = Tileset.Tileset("tileset.png", 32, 32)
        self.tileset.add_tile("grass", 0, 0)
        self.tileset.add_tile("dirt", 0, 32)
        self.tileset.add_tile("stone", 0, 64)
        self.tileset.add_tile("water", 0, 96)
        
        self.width = 10
        self.height = 10
        
        for i in range(0, self.height):
            self.tiles.append(list())
            for j in range(0, self.width):
                if i == 0 or i == self.height-1 or j == 0 or j == self.width-1:  
                    wall = wall_tools.Wall_tiles(j, i)
                    walls.append(wall)                      
                    self.tiles[i].append("stone")  
                else:
                    self.tiles[i].append("grass")
    
    def render(self, screen):
        for y in range(0, int(screen.get_height() / self.tileset.tile_height) +1):
            if y >= self.height or y < 0:
                continue
            line = self.tiles[y]
            for x in range(0, int(screen.get_width() / self.tileset.tile_width) +1):
                if x >= self.width or x < 0:
                    continue
                tilename = line[x]
                tile = self.tileset.get_tile(tilename)
                if tile is not None:
                    screen.blit(self.tileset.image, (x * self.tileset.tile_width, y * self.tileset.tile_height), tile.rect)