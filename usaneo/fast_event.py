import pygame 
from pygame import fastevent
class FastEvent:
    def __init__(self, fast_event_handle, custom_type):
        self.fast_event_handle_handle_core = pygame.USEREVENT + 1.2
        fast_event_handle = fastevent.post(fastevent.Event(fast_event_handle()))
        self.custom = pygame.event.custom_type(custom_type) 
        