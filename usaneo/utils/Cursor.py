import pygame


class Cursor:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load("cursor_none.png"), (12, 12))
        self.root = pygame.display.get_surface()
        self.x = 0
        self.y = 0
        
    def draw_to_screen(self):
        self.root.blit(self.sprite, (self.x, self.y))
        
    def update(self):
        self.x = pygame.mouse.get_pos()[0] 
        self.y = pygame.mouse.get_pos()[1]