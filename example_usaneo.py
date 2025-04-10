import pygame_shaders
import usaneo.core 
def main():
    # glitch_shader = pygame_shaders.Shader(vertex_path="usaneo/glitch.vert", fragment_path="usaneo/glitch.frag")
    screen = usaneo.core.Screen()
    screen.update_screen()
if __name__ == "__main__":
    main()