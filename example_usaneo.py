import usaneo.core 
# import pygame_shaders
from usaneo.utils.Cursor import Cursor

def main():
    # glitch_shader = pygame_shaders.Shader(vertex_path="usaneo/glitch.vert", fragment_path="usaneo/glitch.frag")
    screen = usaneo.core.Screen()
    curs = Cursor()
    applause = usaneo.core.Sound("applause.wav")
    while True:
        keyboard = usaneo.core.KeyBoard()
        curs.update()
        curs.draw_to_screen()
    screen.update_screen()
if __name__ == "__main__":
    main()