import pygame
import random
from constants import *

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Image and Rect
        self.image = pygame.Surface([BALL_WIDTH, BALL_WIDTH])
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        
        self.set_position_and_direction()

    def set_position_and_direction(self):
        # Coordinates for center
        x = SCREEN_WIDTH / 2
        y = random.randint(2 * BALL_WIDTH, SCREEN_HEIGHT - 2 * BALL_WIDTH)
        self.rect.center = [x, y]

        # Random direction
        x_speed = BALL_SPEED * random.choice((-1,1))
        y_speed = BALL_SPEED * random.choice((-1,1))
        self.speed = [x_speed, y_speed]

    def change_x_speed(self):
        self.speed[0] = -1 * self.speed[0]

    def change_y_speed(self):
        self.speed[1] = -1 * self.speed[1]

    def check_collisions(self, player1_bat, player2_bat):
        if self.rect.colliderect(player2_bat.rect) and self.speed[0] > 0:
            if abs(self.rect.right - player2_bat.rect.left) < 10:
                self.change_x_speed()
            elif abs(self.rect.bottom - player2_bat.rect.top) < 10 and self.speed[1] > 0:
                self.change_y_speed()
            elif abs(self.rect.top - player2_bat.rect.bottom) < 10 and self.speed[1] < 0:
                self.change_y_speed()
        elif self.rect.colliderect(player1_bat.rect) and self.speed[0] < 0:
            if abs(self.rect.left - player1_bat.rect.right) < 10:
                self.change_x_speed()
            elif abs(self.rect.bottom - player1_bat.rect.top) < 10 and self.speed[1] > 0:
                self.change_y_speed()
            elif abs(self.rect.top - player1_bat.rect.bottom) < 10 and self.speed[1] < 0:
                self.change_y_speed()

    def round_over(self, player1, player2):
        if self.rect.right >= SCREEN_WIDTH:
            player1.score += 1
            return True
        if self.rect.left <= 0:
            player2.score +=1
            return True
        
        return False

    def reinit(self):
        self.set_position_and_direction()

    def update(self):
        self.rect.move_ip(self.speed)

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.change_y_speed()
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)