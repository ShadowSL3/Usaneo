import pygame
import usaneo.constants as cost

def usaneo_init():
    pygame.init()
    screen = pygame.display.set_mode((cost.Constants.WIDTH, cost.Constants.HEIGHT))
    usaneo_title = pygame.display.set_caption("Usaneo")
class Event: 
    def event(screen):
        screen = pygame.display.set_mode((cost.Constants.WIDTH,cost.Constants.HEIGHT))
        running = True
        while running: 
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    running = False
                    pygame.quit()

def update_Screen():
    pygame.display.update()