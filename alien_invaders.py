import pygame
import sys
import settings as s
from bullet import Bullet
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
    bullets = pygame.sprite.Group()

    while True:
        check_events(spaceship, bullets, screen)
        check_keys_for_moving(spaceship)
        draw_stars(stars)
        screen_update(screen, spaceship, bullets)


def check_events(spaceship, bullets, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            check_keys_for_shooting(spaceship, bullets, screen, event)


def check_keys_for_moving(spaceship):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        spaceship.move(left=True)
    if keys[pygame.K_RIGHT]:
        spaceship.move(right=True)


def check_keys_for_shooting(spaceship, bullets, screen, event):
    if event.key == pygame.K_SPACE:
        if len(bullets) < 5:
            new_bullet = Bullet(screen, spaceship)
            bullets.add(new_bullet)


def screen_update(screen, spaceship, bullets):
    screen.blit(spaceship.image, spaceship.spaceship_rect)
    bullets.update()
    draw_bullets(bullets)
    pygame.display.update()
    screen.fill(color=s.SCREEN_COLOR)


def draw_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.y < 0:
            bullets.remove(bullet)
        else:
            bullet.draw()


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
