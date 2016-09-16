#Main Game File

import pygame
import constants
import socket
import Utils
from time import sleep

def game():
    pygame.init()
    pygame.display.set_caption("Server")

    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    Serv = Utils.Server()
    clock = pygame.time.Clock()

    done = False

    getter = Utils.Utils()

    location = ((0,0), (25,25))
    mousepos = (0,0)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if pygame.mouse.get_pressed() == (1,0,0):
                mousepos = pygame.mouse.get_pos()

        mouse2 = Serv.WaitForConnection()
        location = getter.getLocation(mouse2)

        Serv.sendData(mousepos)

        screen.fill((255,255, 255))
        print "Processed:" + str(location) + ":"
        pygame.draw.rect(screen, constants.BLUE, (mousepos, (25,25)))
        pygame.draw.rect(screen, constants.GREEN, location)
        clock.tick(30)
        pygame.display.flip()

    exit()

game()
