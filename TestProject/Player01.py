#Main Game File

import pygame
import constants
import socket
import Utils

def game():
    pygame.init()
    pygame.display.set_caption("Client")

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

    done = False

    client = Utils.Client()
    getter = Utils.Utils()

    mousepos = (0,0)
    mouse2 = ((0,0), (0, 0))

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if pygame.mouse.get_pressed() == (1,0,0):
                mousepos = pygame.mouse.get_pos()

        screen.fill((255,255, 255))
        pygame.draw.rect(screen, constants.GREEN, (mousepos, (25,25)))
        pygame.draw.rect(screen, constants.BLACK, mouse2)

        client.sendData(mousepos)
        mouse2 = client.recieveData()
        mouse2 = getter.getLocation(mouse2)
        print mousepos

        clock.tick(60)
        pygame.display.flip()

    exit()

game()
