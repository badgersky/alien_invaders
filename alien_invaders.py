import pygame
import sys
import settings as s
from spaceship import Spaceship


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
    if keys[pygame.K_ESCAPE]:
        sys.exit()


if __name__ == '__main__':
    main_loop()
