from usaneo.core import usaneo_init, Event, update_Screen
from usaneo.fast_event import FastEvent
from usaneo.services.audio import Music
import pygame_shaders
def main():
    screen = usaneo_init(800, 600)
    glitch_shader = pygame_shaders.Shader(vertex_path="usaneo/glitch.vert", fragment_path="usaneo/glitch.frag")
    running = True
    while running:
        running = usaneo_handle_events()
        usaneo_update()
        glitch_shader.render()
        
    usaneo_quit()
if __name__ == "__main__":
    main()