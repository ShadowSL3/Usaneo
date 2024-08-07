from usaneo.core import usaneo_init, usaneo_quit, usaneo_update, usaneo_handle_events
from usaneo.sprites import UsaneoSprite, UsaneoFont
def main():
    screen = dont_init(800, 600)
    sprite = UsaneoSprite('path/to/sprite.png')
    font = UsaneoFont('path/to/font.ttf', 24)

    running = True
    while running:
        running = usaneo_handle_events()
        
        screen.fill((255, 255, 255))
        sprite.draw(screen)
        text_surface = font.render("Hello, Usaneo!", (0, 0, 0))
        screen.blit(text_surface, (50, 50))
        
        usaneo_update()
    
    usaneo_quit()

if __name__ == "__main__":
    main()
