from usaneo.core import usaneo_init, Event, update_Screen
from usaneo.sprites import UsaneoSprite, UsaneoFont
from usaneo.fast_event import FastEvent_Core
from usaneo.services.audio import Music
def main():
    screen = usaneo_init(800, 600)
    running = True
    while running:
        running = usaneo_handle_events()
        usaneo_update()
        
    usaneo_quit()
from usaneo.fast_event import FastEvent
from usaneo.services.audio import Music
from usaneo.utils.system import system
import usaneo.constants
import pygame
def main():
    screen = usaneo_init()
    
    while 1: 
        Event.event(screen)

        return True

if __name__ == "__main__":
    main()