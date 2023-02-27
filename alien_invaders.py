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

        spaceship.blit_spaceship()
        pygame.display.flip()
        screen.fill(color=s.SCREEN_COLOR)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


class Spaceship:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/spaceship.bmp')
        self.spaceship = self.image.get_rect()
        screen_rect = self.screen.get_rect()
        self.spaceship.midbottom = screen_rect.midbottom

    def blit_spaceship(self):
        self.screen.blit(self.image, self.spaceship)


if __name__ == '__main__':
    main_loop()
