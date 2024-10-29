import pygame
from Player import Player
from Button import Button
import time
import math
from Network import Network

back_button_image = pygame.image.load('/Users/matthewrosenblum/Downloads/backButt.png')
back_button_image = pygame.transform.scale(back_button_image, (150, 50))
back_button = Button(back_button_image, 100,50)

green_car_image = pygame.image.load('/Users/matthewrosenblum/Downloads/greenTop.png')
green_car_image = pygame.transform.scale(green_car_image, (42.5, 125))

red_car_image = pygame.image.load('/Users/matthewrosenblum/Downloads/redTop.png')
red_car_image = pygame.transform.scale(red_car_image, (42.5, 125))

track_image = pygame.image.load('/Users/matthewrosenblum/Downloads/track.jpg')
track_image = pygame.transform.scale(track_image, (1280, 720))

clock = pygame.time.Clock()
FPS = 60

def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)

class AbstractCar:
    def __init__(self, max_vel, rotation_vel, player):
        self.player = player
        if self.player.car == "green":
            self.IMG = green_car_image
        if self.player.car == "red":
            self.IMG = red_car_image
        self.img = self.IMG
        self.max_vel = max_vel
        self.vel = 0
        self.rotation_vel = rotation_vel
        self.angle = -90
        self.x, self.y = self.START_POS
        self.acceleration = 0.1


    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.rotation_vel
        elif right:
            self.angle -= self.rotation_vel

    def draw(self, win):
        blit_rotate_center(win, self.img, (self.x, self.y), self.angle)

    def move_forward(self):
        self.vel = min(self.vel + self.acceleration, self.max_vel)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.vel
        horizontal = math.sin(radians) * self.vel

        self.y -= vertical
        self.x -= horizontal

    def reduce_speed(self):
        self.vel = max(self.vel - self.acceleration / 2, 0)
        self.move()


class PlayerCar(AbstractCar):
    START_POS = (550, 575)

def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])

class Play:
    def __init__(self, screen, player):
        self.screen = screen
        self.player = player
        self.player_car = PlayerCar(4,4, self.player)
        pygame.display.set_caption('Play')
    def run(self):
        # n = Network()
        # startPos = readPos(n.getPos())

        while True:
            clock.tick(FPS)

            self.screen.blit(track_image, (0, 0))
            back_button.update(self.screen)
            self.player_car.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    backButt = back_button.checkForInput(pos)
                    if backButt:
                        return True

            keys = pygame.key.get_pressed()
            moved = False

            if keys[pygame.K_a]:
                self.player_car.rotate(left=True)
            if keys[pygame.K_d]:
                self.player_car.rotate(right=True)
            if keys[pygame.K_w]:
                moved = True
                self.player_car.move_forward()

            if not moved:
                self.player_car.reduce_speed()

            pygame.display.update()
