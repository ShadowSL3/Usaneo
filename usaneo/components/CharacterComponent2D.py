import pygame
class CharacterComponent:
    def __init__(self):
        self.sprite = pygame.Surface((32, 32))
        self.Image = pygame.image.load()
        self.transform = pygame.Vector2(0,0)
        self.speed = 5
    def move_left(self):
        self.transform. -= self.speed
    
    def draw(self, surface):
        self.sprite.blit(surface)