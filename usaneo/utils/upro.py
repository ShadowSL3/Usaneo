import pygame 

uprovec = pygame.math.Vector2
urovec3 = pygame.math.Vector3
class UPRO():
    def __init__(self):
        super().__init__()
        self.image = pygame.sprite.Sprite()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        