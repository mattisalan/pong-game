import pygame
from constants import *


class Bat(pygame.sprite.Sprite):

    def __init__(self, isPlayer1):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([BAT_WIDTH, BAT_HEIGTH])
        self.image.fill(GREY)
        self.rect = self.image.get_rect()
        if isPlayer1:
            self.rect.center = (15, SCREEN_HEIGHT / 2)
        else: 
            self.rect.center = (SCREEN_WIDTH - 15, SCREEN_HEIGHT / 2)

        self.pos_y = self.rect.y
        self.speed = 0
        self.score = 0

    def move_up(self, dt):
        if self.rect.top > 0:
            self.pos_y -= BAT_SPEED * dt
            self.rect.y = round(self.pos_y)
        else:
            self.rect.top = 0

    def move_down(self, dt):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.pos_y += BAT_SPEED * dt
            self.rect.y = round(self.pos_y)
        else:
            self.rect.bottom = SCREEN_HEIGHT
        