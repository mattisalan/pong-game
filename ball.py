from typing import Any
import pygame
from constants import *

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # Image and Rect
        self.image = pygame.Surface([BALL_WIDTH, BALL_WIDTH])
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        self.rect.center = [SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2]

        self.speed = BALL_SPEED

    def update(self):
        self.rect.move_ip(self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)