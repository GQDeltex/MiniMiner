import pygame
import Player
import constants
import wall_tools
import Tilemap
import sys
import Utils


pygame.init()
screen = pygame.display.set_mode(constants.SCREENRES)
pygame.display.set_caption("Little Miners")
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(constants.WHITE)
clock = pygame.time.Clock()
DEFAULT_FONT = "Comic Sans MS"
SMALLFONT = pygame.font.SysFont(DEFAULT_FONT, 25)
MEDIUMFONT = pygame.font.SysFont(DEFAULT_FONT, 40)
BIGFONT = pygame.font.SysFont(DEFAULT_FONT, 55)

def menu():
    menu = True
    connect = False
    global network
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                menu = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    connect = True
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                    menu = False
        screen.fill(constants.WHITE)
        Utils.TextToScreen("Welcome to Little Miners!", constants.GREEN, -150, BIGFONT, screen)
        Utils.TextToScreen("This game can be played by two people or alone." , constants.BLACK, -30, SMALLFONT, screen)
        Utils.TextToScreen("You can move with the Arrow-Keys.", constants.BLACK, 10, SMALLFONT, screen)
        Utils.TextToScreen("Press 'Space' to connect/play and 'Escape' to exit", constants.BLACK, 50, SMALLFONT, screen)
        Utils.TextToScreen("Warning: you can't do anything while connecting!", constants.BLACK, 90, SMALLFONT, screen)
        if connect:
            Utils.TextToScreen("Connecting...", constants.RED, 130, SMALLFONT, screen)
            if constants.MULTIPLAYER:
                if constants.SERVER:
                    network = Utils.Server()
                else:
                    network = Utils.Client()
            else:
                network = None
            menu = False

        pygame.display.update()
        clock.tick(15)



def main():
    done = False

    score = 0

    all_sprite_list = pygame.sprite.Group()

    player_01 = Player.Player(100, 100, 32, 0, 32, 32, network)
    all_sprite_list.add(player_01)
    if constants.MULTIPLAYER:
        player_02 = Player.Player(70, 70, 32, 64, 32, 96, network)
        all_sprite_list.add(player_02)

    wall_list = list()

    map = Tilemap.Tilemap(wall_list)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
                if event.key == pygame.K_LEFT:
                    player_01.changespeed(-1, 0)
                    player_01.changedirection("LEFT")
                elif event.key == pygame.K_RIGHT:
                    player_01.changespeed(1, 0)
                    player_01.changedirection("RIGHT")
                elif event.key == pygame.K_UP:
                    player_01.changespeed(0, -1)
                    player_01.changedirection("UP")
                elif event.key == pygame.K_DOWN:
                    player_01.changespeed(0, 1)
                    player_01.changedirection("DOWN")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player_01.changespeed(1, 0)
                elif event.key == pygame.K_RIGHT:
                    player_01.changespeed(-1, 0)
                elif event.key == pygame.K_UP:
                    player_01.changespeed(0, 1)
                elif event.key == pygame.K_DOWN:
                    player_01.changespeed(0, -1)

        screen.fill(constants.BLACK)
        map.render(screen)
        player_01.update(wall_list)
        if constants.MULTIPLAYER:
            if constants.SERVER:
                player_01.sendData()
                player_02.getData()
            else:
                player_02.getData()
                player_01.sendData()
            player_02.update(wall_list)
        all_sprite_list.draw(screen)
        clock.tick(60)
        pygame.display.flip()

if __name__ == '__main__':
    menu()
    main()
    pygame.quit()
    sys.exit()
