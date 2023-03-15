import pygame
import sys
import settings as s
from bullet import Bullet
from spaceship import XWing
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
    x_wing = XWing(screen)
    stars = create_stars(screen)
    bullets = pygame.sprite.Group()

    while True:
        check_events(x_wing, bullets, screen)
        x_wing.move()
        draw_bullets(bullets)
        draw_stars(stars)
        screen_update(screen, x_wing, bullets)


def check_events(x_wing, bullets, screen):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(x_wing, bullets, screen, event)
        if event.type == pygame.KEYUP:
            check_keyup_events(x_wing, event)


def check_keydown_events(x_wing, bullets, screen, event):
    if event.key == pygame.K_ESCAPE:
        sys.exit()
    if event.key == pygame.K_SPACE:
        if len(bullets) < 5:
            new_bullet = Bullet(screen, x_wing)
            bullets.add(new_bullet)
    if event.key == pygame.K_LEFT:
        x_wing.moving_left = True
    if event.key == pygame.K_RIGHT:
        x_wing.moving_right = True


def check_keyup_events(x_wing, event):
    if event.key == pygame.K_LEFT:
        x_wing.moving_left = False
    if event.key == pygame.K_RIGHT:
        x_wing.moving_right = False


def screen_update(screen, x_wing, bullets):
    x_wing.update()
    bullets.update()
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
