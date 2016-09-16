import pygame
import constants

class SpriteSheet():
    sprite_sheet = None
    
    def __init__(self, file_name):
        self.sprite_sheet = pygame.image.load(file_name).convert()
    
    def getImage(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image.set_colorkey(constants.COLORKEY)
        return image
    
class TextToScreen(object):
    def __init__(self, msg, color, y_displace, font, screen):
        textSurf, textRect = self.text_objects(msg, color, font)
        textRect.center = (constants.SCREENWIDTH/2), (constants.SCREENHEIGHT/2) + y_displace
        screen.blit(textSurf, textRect)

    def text_objects(self, text, color, size):
        textSurface = size.render(text, True, color)
        return textSurface, textSurface.get_rect()  