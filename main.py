import pygame
from pygame.locals import *
from constants import *
from bat import Bat

def main():
    pygame.init()
    clock = pygame.time.Clock()
    

    # Game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create game objects
    player1_bat = Bat(isPlayer1=True)
    player2_bat = Bat(isPlayer1=False)

    # Sprite groups
    player_bats = pygame.sprite.Group()
    player_bats.add(player1_bat, player2_bat)

    # GAME LOOP
    while True:

        # EVENTS / PLAYER INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    player1_bat.move_up()
                if event.key == pygame.K_s:
                    player1_bat.move_down()
                if event.key == pygame.K_UP:
                    player2_bat.move_up()
                if event.key == pygame.K_DOWN:
                    player2_bat.move_down()
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    player1_bat.move_down()
                if event.key == pygame.K_s:
                    player1_bat.move_up()
                if event.key == pygame.K_UP:
                    player2_bat.move_down()
                if event.key == pygame.K_DOWN:
                    player2_bat.move_up()
            

        # GAME LOGIC

        # RENDER GRAPHICS
        screen.fill(BG_COLOR)
        player_bats.update()
        player_bats.draw(screen)

        pygame.display.flip() # Refresh screen

        clock.tick(60) # Frame rate

if __name__ == "__main__":
    main()