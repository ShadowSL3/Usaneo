import pygame
class UPRO():
    def __init__(self):
        super().__init__()
        self.image = pygame.sprite.Sprite()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
