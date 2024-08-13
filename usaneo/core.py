import pygame
def usaneo_init():
    pygame.init()
    screen = pygame.display.set_mode(())
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

def usaneo_display_flip(flip_screen):
    flip_screen = pygame.display.flip()
def usaneo_update():
    pygame.display.update

def Usaneo_audio_handle_event(self, audio_usaneo, usaneo_mixer_load_music, usaneo_mixer_load_sound):
    self.audio_usaneo = pygame.mixer.music.load(filename=())
def usaneo_handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == Usaneo_audio_handle_event:
            Usaneo_audio_handle_event(audio_usaneo=())
    return True
