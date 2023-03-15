import pygame
import settings as s


class XWing:

    def __init__(self, screen):
        self.image = self.load_image_of_spaceship()
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.speed = s.SPACESHIP_SPEED

        self.rect.midbottom = self.screen_rect.midbottom
        self.spaceship_x_float = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def move(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.spaceship_x_float += self.speed
            self.rect.x = self.spaceship_x_float
        if self.moving_left and self.rect.left > 0:
            self.spaceship_x_float -= self.speed
            self.rect.x = self.spaceship_x_float

    def update(self):
        self.screen.blit(self.image, self.rect)

    @staticmethod
    def load_image_of_spaceship():
        image = pygame.image.load('images/x-wing.bmp')
        return image


class TieFighter(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super().__init__()
        self.image = self.load_image_of_spaceship()
        self.rect = self.image.get_rect()
        self.screen = screen

        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.screen.blit(self.image, self.rect)

    @staticmethod
    def load_image_of_spaceship():
        image = pygame.image.load('images/tie_fighter.bmp')
        return image


if __name__ == '__main__':
    pass
