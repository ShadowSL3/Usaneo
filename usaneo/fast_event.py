import pygame 
from pygame import fastevent
class FastEvent_Core:
    def __init__(self, fast_event_handle):
        self.fast_event_handle_handle_core = pygame.USEREVENT + 1.2
        fast_event_handle = fastevent.post(fastevent.Event(fast_event_handle()))