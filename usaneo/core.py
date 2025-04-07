import pygame


def usaneo_init(self, width=480, height=272):
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    return screen

def Useneo_physics():
    pass    
def USR2D():
    pass
def Camera2D():
    pygame.camera.init()
    camera_dev = pygame.camera.list_cameras()[-1]
    cam = pygame.camera.Camera(camera_dev)
def usaneo_filler(fill_object):
    fill_objecter = usaneo_init().fill(color=())
def usaneo_quit():
    pygame.quit()
def Usaneo_Vec2(self, scales):
    self.scales = pygame.transform.scale(self.scales, (50,50))
    
class Event: 
    def event(screen, width=480, height=272):
        screen = pygame.display.set_mode((width, height))
        running = True
        while running: 
            for evt in pygame.event.get():
                if evt.type == pygame.QUIT:
                    running = False
                    pygame.quit()

def update_Screen():
    pygame.display.flip()