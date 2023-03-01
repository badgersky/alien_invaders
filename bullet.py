import pygame
import settings as s


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, spaceship):
        super().__init__()
        self.screen = screen
        self.spaceship_rect = spaceship.spaceship_rect

        position = self.spaceship_rect.midtop
        self.rect = pygame.Rect(position, (s.BULLET_SIZE['width'], s.BULLET_SIZE['height']))

        self.speed = s.BULLET_SPEED

    def draw_bullets(self):
        pygame.draw.rect(self.screen, s.BULLET_COLOR, self.rect)

    def move(self):
        self.rect.y -= self.speed


if __name__ == '__main__':
    pass
