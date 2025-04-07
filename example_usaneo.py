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
if __name__ == "__main__":
    main()