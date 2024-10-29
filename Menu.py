import pygame
from Button import Button

background_image = pygame.image.load("/Users/matthewrosenblum/Downloads/blurCheck.png")

button_surface1 = pygame.image.load("/Users/matthewrosenblum/Downloads/optButt.png")
button_surface1 = pygame.transform.scale(button_surface1,(300,100))
button1 = Button(button_surface1,640,380)

button_surface2 = pygame.image.load("/Users/matthewrosenblum/Downloads/startButt.png")
button_surface2 = pygame.transform.scale(button_surface2,(300,100))
button2 = Button(button_surface2,640,150)

button_surface3 = pygame.image.load("/Users/matthewrosenblum/Downloads/quitButt.png")
button_surface3 = pygame.transform.scale(button_surface3,(300,100))
button3 = Button(button_surface3,640,620)

class Menu:
    def __init__(self, screen):
        self.screen = screen
        pygame.display.set_caption("Menu")
    def run(self):
        while True:
            #self.screen.fill("white")
            self.screen.blit(background_image,(0,0))
            button1.update(self.screen)
            button2.update(self.screen)
            button3.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    optButt = button1.checkForInput(pos)
                    startButt = button2.checkForInput(pos)
                    quitButt = button3.checkForInput(pos)
                    if optButt:
                        print("Option Button Clicked")
                        return 1
                    if startButt:
                        print("Start Button Clicked")
                        return 2
                    if quitButt:
                        print("Quit Button Clicked")
                        return 3


            pygame.display.update()