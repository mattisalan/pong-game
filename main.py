import time

import pygame
from pygame.locals import *

from constants import *
from bat import Bat
from ball import Ball


def update_scores(player1_score, player2_score, screen):
    font = pygame.font.SysFont(FONT, FONTSIZE)
    text = font.render(f"{player1_score} - {player2_score}", True, GREY)
    text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, 50))

    screen.blit(text, text_rect)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    prev_time = time.time()

    # Game window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create game objects
    player1_bat = Bat(isPlayer1=True)
    player2_bat = Bat(isPlayer1=False)
    ball = Ball()

    # Sprite groups
    player_bats = pygame.sprite.Group()
    player_bats.add(player1_bat, player2_bat)

    # GAME LOOP
    while True:

        # Delta time
        time_now = time.time()
        dt = time_now - prev_time
        prev_time = time_now

        # EVENTS / PLAYER INPUTS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
            
        keys = pygame.key.get_pressed()
        if keys[K_w]:
            player1_bat.move_up(dt)
        if keys[K_s]:
            player1_bat.move_down(dt)
        if keys[K_UP]:
            player2_bat.move_up(dt)
        if keys[K_DOWN]:
            player2_bat.move_down(dt)

        # GAME LOGIC
        ball.update(dt)

        ball.check_collisions(player1_bat, player2_bat)

        if ball.round_over(player1_bat, player2_bat):
            ball.reinit()

        # RENDER GRAPHICS
        screen.fill(BG_COLOR)
        update_scores(player1_bat.score, player2_bat.score, screen)
        player_bats.draw(screen)
        ball.draw(screen)

        pygame.display.flip() # Refresh screen

        clock.tick(FPS_LIMIT)

if __name__ == "__main__":
    main()