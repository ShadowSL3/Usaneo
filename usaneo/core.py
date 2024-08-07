import pygame

def usaneo_init(width, height):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    return screen

def usaneo_quit():
    pygame.quit()

def usaneo_update():
    pygame.display.flip()

def usaneo_handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True
