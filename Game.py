import pygame
import sys
from Menu import Menu
from Options import Options
from Player import Player
from Play import Play

screen = pygame.display.set_mode((1280, 720))

class Game:
    def __init__(self):
        pygame.init()
        self.isMenu = True
        self.isOption = False
        self.isStart = False
        self.player = Player()
    def run(self):
        while True:
            if self.isMenu:
                menu = Menu(screen)
                result = menu.run()
                print(f"Result is {result}")
                if result == 3:
                    pygame.quit()
                    sys.exit()
                if result == 1:
                    self.isMenu = False
                    self.isOption = True
                    self.isStart = False
                if result == 2:
                    self.isMenu = False
                    self.isStart = True
                    self.isOption = False
            if self.isOption:
                option = Options(screen, self.player)
                done = option.run()
                if done:
                    self.isOption = False
                    self.isMenu = True
            if self.isStart:
                start = Play(screen, self.player)
                done = start.run()
                if done:
                    self.isStart = False
                    self.isMenu = True

