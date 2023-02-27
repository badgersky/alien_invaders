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
        check_events(spaceship)

        spaceship.blit_spaceship()
        pygame.display.flip()
        screen.fill(color=s.SCREEN_COLOR)


def check_events(spaceship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, spaceship)


def check_keydown_events(event, spaceship):
    if event.type == pygame.K_RIGHT:
        spaceship.move(right=True)
    if event.type == pygame.K_LEFT:
        spaceship.move(left=True)


class Spaceship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/spaceship.bmp')
        self.spaceship = self.image.get_rect()
        screen_rect = self.screen.get_rect()
        self.spaceship.midbottom = screen_rect.midbottom
        self._moving_right = False
        self._moving_left = False

    @property
    def moving_right(self):
        return self._moving_right

    @moving_right.setter
    def moving_right(self, is_moving):
        self._moving_right = is_moving

    @property
    def moving_left(self):
        return self._moving_left

    @moving_left.setter
    def moving_left(self, is_moving):
        self._moving_left = is_moving

    def blit_spaceship(self):
        self.screen.blit(self.image, self.spaceship)

    def move(self, right=False, left=False):
        if right:
            self.spaceship.x += s.SPACESHIP_SPEED
        if left:
            self.spaceship.x -= s.SPACESHIP_SPEED


if __name__ == '__main__':
    main_loop()
