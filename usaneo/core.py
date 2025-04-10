import pygame

pygame.init()
pygame.display.set_caption("Usaneo")


class Screen:
    def __init__(self, width=480, height=272):
        self.screen = pygame.display.set_mode((width, height))
        
    def blit(self, img, sx=0, sy=0, sw=-1, sh=-1, dx=-1, dy=-1, blend=False, dw=-1, dh=-1):
        rect = img.get_rect()
        w, h = rect.width, rect.height

        if sw == -1:
            sw = w
        if sh == -1:
            sh = h
        if dx == -1:
            dx = sx
        if dy == -1:
            dy = sy
        if dw == -1:
            dw = w
        if dh == -1:
            dh = h

        tmp = img.subsurface(sx, sy, sw, sh)
        if dw != w or dh != h:
            tmp = pygame.transform.scale(tmp, (dw, dh))
        self.screen.blit(tmp, (dx, dy))
    
    def update_screen(self):
        pygame.display.flip()
        pygame.event.pump()
    
    def clear_screen(self, color):
        self.screen.fill(color)
        

class Image(pygame.Surface):
    def __init__(self, *args):
        if len(args) == 2:
            pygame.Surface.__init__(self, (args[1], args[0]), pygame.SRCALPHA, 32)
            self.set_alpha(255)
        else:
            if isinstance(args[0], Image):
                surf = args[0]
            else:
                surf = pygame.image.load(args[0])
                pygame.Surface.__init__(self, (surf.get_width(), surf.get_height()), pygame.SRCALPHA, 32)
                self.blit(surf, surf.get_rect())

    def clear(self, color):
        self.fill(color)

    def blit(self, src, sx=0, sy=0, w=-1, h=-1, dx=0, dy=0, blend=False):
        if isinstance(dx, float) or isinstance(dy, float):
            print("dx or dy is float, should be integer")
            return

        if isinstance(sx, tuple):
            pygame.Surface.blit(self, src, sx)
            return

        if dx == -1:
            dx = sx
        if dy == -1:
            dy = sy

        if w == -1: 
            w = src.get_width()
        if h == -1: 
            h = src.get_height()

        tmp = src.subsurface(sx, sy, w, h)
        pygame.Surface.blit(self, tmp, (dx, dy))

    @property
    def width(self):
        return self.get_width()

    @property
    def height(self):
        return self.get_height()