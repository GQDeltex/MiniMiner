import pygame
import constants
import Animation
from Utils import *

class Player(pygame.sprite.Sprite):
    change_x = 0
    change_y = 0

    def __init__(self, x, y, coords_right_x, coords_right_y, coords_up_x, coords_up_y, server, client):
        self.left_frames = []
        self.right_frames = []
        self.up_frames = []
        self.down_frames = []

        self.server = server
        self.client = client
        self.utils = Utils()

        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("tileset.png")

        image = sprite_sheet.getImage(coords_right_x, coords_right_y, 32, 32)
        self.right_frames.append(image)
        image = sprite_sheet.getImage(coords_right_x + 32, coords_right_y, 32, 32)
        self.right_frames.append(image)

        image = sprite_sheet.getImage(coords_right_x, coords_right_y, 32, 32)
        image = pygame.transform.flip(image, True, False)
        self.left_frames.append(image)
        image = sprite_sheet.getImage(coords_right_x + 32, coords_right_y, 32, 32)
        image = pygame.transform.flip(image, True, False)
        self.left_frames.append(image)

        image = sprite_sheet.getImage(coords_up_x, coords_up_y, 32, 32)
        self.up_frames.append(image)
        image = sprite_sheet.getImage(coords_up_x + 32, coords_up_y, 32, 32)
        self.up_frames.append(image)

        image = sprite_sheet.getImage(coords_up_x, coords_up_y, 32, 32)
        image = pygame.transform.flip(image, False, True)
        self.down_frames.append(image)
        image = sprite_sheet.getImage(coords_up_x + 32, coords_up_y, 32, 32)
        image = pygame.transform.flip(image, False, True)
        self.down_frames.append(image)


        self.image = self.right_frames[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.direction = 1
        self.anim = Animation.Animation(10)
        self.time = 0
        self.current = 0

    def changespeed(self, x, y):
        self.change_x += x
        self.change_y += y

    def changedirection(self, direction):
        if direction == "RIGHT":
            self.direction = 1
            self.current = 0
        elif direction == "LEFT":
            self.direction = -1
            self.current = 0
        elif direction == "UP":
            self.direction = 99
            self.current = 0
        elif direction == "DOWN":
            self.direction = -99
            self.current = 0
        else:
            self.direction = 0
            self.current = 0

    def update(self, walls):
        if self.direction == 1:
            self.image = self.anim.update(self.right_frames)
        if self.direction == -1:
            self.image = self.anim.update(self.left_frames)
        if self.direction == 99:
            self.image = self.anim.update(self.up_frames)
        if self.direction == -99:
            self.image = self.anim.update(self.down_frames)

        self.rect.x += self.change_x
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom

    def sendData(self):
        tosend = (self.rect.x, self.rect.y, self.direction)
        if constants.SERVER:
            self.server.sendData(tosend)
        else:
            self.client.sendData(tosend)

    def getData(self):
        if constants.SERVER:
            self.location = self.server.getData()
            self.location,  self.direction = self.utils.getLocation(self.location)
            self.rect.x, self.rect.y = self.location
        else:
            self.location = self.client.getData()
            self.location, self.direction = self.utils.getLocation(self.location)
            self.rect.x, self.rect.y = self.location
