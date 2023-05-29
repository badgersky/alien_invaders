import random

import pygame
import settings as s


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, spaceship, color):
        super().__init__()
        self.color = color
        self.screen = screen
        self.spaceship_rect = spaceship.rect
        position = self.spaceship_rect.center
        self.rect = pygame.Rect(position, (s.BULLET_SIZE['width'], s.BULLET_SIZE['height']))

        self.speed = s.BULLET_SPEED

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class XWingBullet(Bullet):

    def __init__(self, screen, spaceship):
        super().__init__(screen, spaceship, s.BULLET_COLOR)
        self.rect.midbottom = self.spaceship_rect.midtop

    def update(self):
        self.rect.y -= self.speed


class TieFighterBullet(Bullet):
    def __init__(self, screen, spaceship):
        super().__init__(screen, spaceship, s.ENEMY_BULLET_COLOR)
        self.rect.midtop = self.spaceship_rect.midbottom

    def update(self):
        self.rect.y += self.speed


if __name__ == '__main__':
    pass
