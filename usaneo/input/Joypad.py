import pygame 
class UsaneoJoyPad:
    def __init__(self, usaneojoy):
        self.usaneoJoy = pygame.JOYAXISMOTION(usaneojoy)
        self.joyup= pygame.JOYBUTTONUP()
        self.joydown = pygame.JOYBUTTONDOWN()