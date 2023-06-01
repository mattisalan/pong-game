import pygame
from pygame.locals import *
from constants import *

def main():
    pygame.init()

    # Game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # GAME LOOP
    while True:

        # EVENTS / PLAYER INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        # GAME LOGIC

        # RENDER GRAPHICS
        screen.fill(BG_COLOR)

        pygame.display.flip() # Refresh screen

if __name__ == "__main__":
    main()