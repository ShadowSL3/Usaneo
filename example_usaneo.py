from usaneo.core import usaneo_init, usaneo_quit, usaneo_update, usaneo_handle_events, bg_color
from usaneo.sprites import UsaneoSprite, UsaneoFont
from usaneo.fast_event import FastEvent_Core
from usaneo.services.audio import Music
from usaneo.utils.maths import Vec3
def main():
    screen = usaneo_init(width=400, height=500)
    running = True
    while running:
        running = usaneo_handle_events()
        usaneo_update()
        Vec3(vec3=0, value_clamp=10, min_clamp=5, max=30)
    usaneo_quit()

if __name__ == "__main__":
    main()