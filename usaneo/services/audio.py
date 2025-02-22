import pygame

class UsaneoAudioInit:
    def __init__(self, usaneo_Audio_Init):
        self.usaneo_Audio_Init = pygame.mixer.init()
def Music(self, music_init, filename, play_music):
    self.music_init = pygame.mixer.music.load(filename)
    self.music_play = pygame.mixer.music.play(music_init)
    
def Sound(self, sound_init):

    self.soundInit = pygame.mixer.Sound(file=())
    self.init_sound = pygame.mixer.Sound().play(sound_init)
    self.soundInit = pygame.mixer.Sound()
    self.init_sound = pygame.mixer.Sound().play(sound_init)

class Audio_Multiply:
    def __init__(self, audio_multiply_init, db, file) -> None:
        self.audio_init_multiply = pygame.mixer.get_init(audio_multiply_init)
        self.db = pow(10, -6/20)
        self.file = ""