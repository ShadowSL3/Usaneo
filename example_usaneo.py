from usaneo.core import usaneo_init, usaneo_quit, usaneo_update, usaneo_handle_events
from usaneo.sprites import UsaneoSprite, UsaneoFont
from usaneo.fast_event import FastEvent_Core
from usaneo.services.audio import Music
from usaneo.utils.system import system
import usaneo.constants
def main():
    screen = usaneo_init()
    running = True
    while running:
        running = usaneo_handle_events()
        usaneo_update()
    usaneo_quit()

if __name__ == "__main__":
    main()