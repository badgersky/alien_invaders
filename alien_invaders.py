import pygame
import sys
import settings as s


def video_init():
    pygame.init()
    width = s.SCREEN_SIZE['width']
    height = s.SCREEN_SIZE['height']
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Alien Invaders')
    return screen


def main_loop():
    screen = video_init()
    spaceship = Spaceship(screen)

    while True:
        check_events()
        check_key_pressed_events(spaceship)

        screen.blit(spaceship.image, spaceship.spaceship_rect)
        pygame.display.update()
        screen.fill(color=s.SCREEN_COLOR)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def check_key_pressed_events(spaceship):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.move(left=True)
    if keys[pygame.K_RIGHT]:
        spaceship.move(right=True)


class Spaceship:

    def __init__(self, screen):
        self.image = self.load_image_of_spaceship()
        self.spaceship_rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.speed = s.SPACESHIP_SPEED

        self.spaceship_rect.midbottom = self.screen_rect.midbottom
        self.spaceship_x_float = float(self.spaceship_rect.x)

    def move(self, right=False, left=False):
        if right and self.spaceship_rect.right < self.screen_rect.right:
            self.spaceship_x_float += self.speed
            self.spaceship_rect.x = self.spaceship_x_float
        if left and self.spaceship_rect.left > 0:
            self.spaceship_x_float -= self.speed
            self.spaceship_rect.x = self.spaceship_x_float

    @staticmethod
    def load_image_of_spaceship():
        image = pygame.image.load('images/spaceship.bmp')
        return image


if __name__ == '__main__':
    main_loop()
