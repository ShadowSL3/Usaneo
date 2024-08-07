import pygame

class UsaneoSprite:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class UsaneoFont:
    def __init__(self, font_path, size):
        self.font = pygame.font.Font(font_path, size)

    def render(self, text, color):
        return self.font.render(text, True, color)
