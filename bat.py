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
        self.score = 0

    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= BAT_SPEED
        else:
            self.rect.top = 0

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += BAT_SPEED
        else:
            self.rect.bottom = SCREEN_HEIGHT
        