from typing import Any
import pygame
from constants import *

class Bat(pygame.sprite.Sprite):

    def __init__(self, isPlayer1):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([BAT_WIDTH, BAT_HEIGTH])
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        if isPlayer1:
            self.rect.center = (BAT_WIDTH, SCREEN_HEIGHT / 2)
        else: 
            self.rect.center = (SCREEN_WIDTH - BAT_WIDTH, SCREEN_HEIGHT / 2)

        self.speed = 0

    def move_up(self):
        self.speed -= BAT_SPEED

    def move_down(self):
        self.speed += BAT_SPEED

    def update(self):
        self.rect.move_ip([0, self.speed])

        # Do not let the bat go out of screen
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        