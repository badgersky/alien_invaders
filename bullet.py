import random

import pygame
import settings as s


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, color):
        super().__init__()
        self.color = color
        self.screen = screen

        self.speed = s.BULLET_SPEED


class XWingBullet(Bullet):

    def __init__(self, screen, spaceship):
        super().__init__(screen, s.BULLET_COLOR)
        self.spaceship_rect = spaceship.rect
        position = self.spaceship_rect.midtop
        self.rect = pygame.Rect(position, (s.BULLET_SIZE['width'], s.BULLET_SIZE['height']))

    def update(self):
        self.rect.y -= self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


class TieFighterBullet(Bullet):
    def __init__(self, screen):
        super().__init__(screen, s.ENEMY_BULLET_COLOR)
        position = (random.randint(0, s.SCREEN_SIZE['width']), 0)
        self.rect = pygame.Rect(position, (s.BULLET_SIZE['width'], s.BULLET_SIZE['height']))

    def update(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


if __name__ == '__main__':
    pass
