import pygame
from constants import *

class Bat(pygame.sprite.Sprite):

    def __init__(self, isPlayer1):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([BAT_WIDTH, BAT_HEIGTH])
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        if isPlayer1:
            self.rect.center = (2* BAT_WIDTH, SCREEN_HEIGHT / 2)
        else: 
            self.rect.center = (SCREEN_WIDTH - 2 * BAT_WIDTH, SCREEN_HEIGHT / 2)
