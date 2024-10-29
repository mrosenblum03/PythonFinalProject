import pygame
from Button import Button

back_button_image = pygame.image.load('/Users/matthewrosenblum/Downloads/backButt.png')
back_button_image = pygame.transform.scale(back_button_image, (300, 100))
back_button = Button(back_button_image, 150,50)

equip_image = pygame.image.load('/Users/matthewrosenblum/Downloads/equipButt.png')
equip_image = pygame.transform.scale(equip_image, (300, 100))
equip = Button(equip_image, 640,220)

equipped_image = pygame.image.load("/Users/matthewrosenblum/Downloads/equipped.png")
equipped_image = pygame.transform.scale(equipped_image, (300, 100))

green_car_image = pygame.image.load('/Users/matthewrosenblum/Downloads/greenCar.png')
green_car_image = pygame.transform.scale(green_car_image, (1000, 400))

red_car_image = pygame.image.load('/Users/matthewrosenblum/Downloads/redCar.png')
red_car_image = pygame.transform.scale(red_car_image, (1000, 400))

background_image = pygame.image.load('/Users/matthewrosenblum/Downloads/carBackground.png')

right_arrow_image = pygame.image.load('/Users/matthewrosenblum/Downloads/rightArrow.png')
right_arrow_image = pygame.transform.scale(right_arrow_image, (150, 150))

left_arrow_image = pygame.image.load('/Users/matthewrosenblum/Downloads/leftArrow.png')
left_arrow_image = pygame.transform.scale(left_arrow_image, (150, 150))

right_arrow = Button(right_arrow_image, 1100,300)
left_arrow = Button(left_arrow_image, 100,300)

class Options:
    def __init__(self, screen, player):
        self.screen = screen
        self.car1 = True
        self.car2 = False
        self.player = player
        pygame.display.set_caption("Options")
    def run(self):
        while True:
            if self.car1:
                self.screen.blit(background_image, (0, 0))
                self.screen.blit(green_car_image, (150, 300))
                if self.player.car == "green":
                    self.screen.blit(equipped_image, (500, 200))
                else:
                    equip.update(self.screen)
                right_arrow.update(self.screen)
                back_button.update(self.screen)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        backButt = back_button.checkForInput(pos)
                        rightButt = right_arrow.checkForInput(pos)
                        equipButt = equip.checkForInput(pos)
                        if backButt:
                            return True
                        if rightButt:
                            print("Going to next car!")
                            self.car1 = False
                            self.car2 = True
                        if equipButt:
                            print("Car Equipped")
                            self.player.car = "green"
            if self.car2:
                self.screen.blit(background_image, (0, 0))
                self.screen.blit(red_car_image, (150, 300))
                left_arrow.update(self.screen)
                back_button.update(self.screen)
                if self.player.car == "red":
                    self.screen.blit(equipped_image, (500, 200))
                else:
                    equip.update(self.screen)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        backButt = back_button.checkForInput(pos)
                        leftButt = left_arrow.checkForInput(pos)
                        equipButt = equip.checkForInput(pos)
                        if backButt:
                            return True
                        if leftButt:
                            print("Going to next car!")
                            self.car2 = False
                            self.car1 = True
                        if equipButt:
                            print("Car Equipped")
                            self.player.car = "red"