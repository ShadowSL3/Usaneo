import pygame

class UsaneoKeyboard:
    def __init(self, key, space, backspace, K, A):
        self.key = pygame.KEYDOWN(key)
        self.space = pygame.K_SPACE(space)
        self.backspace = pygame.K_BACKSPACE(backspace)
        self.A = pygame.K_a(A)
        self.K = pygame.K_k(K)
    def Event_Keyboard(self):
        for event in pygame.event.get():
            if event.type == self.A:
                return False
            if event.type == self.key:
                return pygame.K_a()
            if event.type == self.space:
               pygame.K_SPACE(self.space)
               return False
            if event.type == self.K:
                pygame.K_k(self.K)
                return False
                