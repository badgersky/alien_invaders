import pygame
import sys
import settings as s
from spaceship import Spaceship
from star import Star


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
    stars = create_stars(screen)

    while True:
        check_events()
        check_key_pressed_events(spaceship)
        draw_stars(stars)
        screen_update(screen, spaceship)


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


def screen_update(screen, spaceship):
    screen.blit(spaceship.image, spaceship.spaceship_rect)
    pygame.display.update()
    screen.fill(color=s.SCREEN_COLOR)


def draw_stars(stars):
    for star in stars:
        star.draw_star()


def create_stars(screen):
    stars = pygame.sprite.Group()
    for _ in range(1000):
        star = Star(screen)
        stars.add(star)
    return stars


if __name__ == '__main__':
    main_loop()
