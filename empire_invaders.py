import pygame
import sys
import settings as s
from bullet import XWingBullet, TieFighterBullet
from spaceship import XWing, TieFighter
from star import Star


def video_init():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption('Empire Invaders')
    s.SCREEN_SIZE['width'] = screen.get_width()
    s.SCREEN_SIZE['height'] = screen.get_height()
    return screen


def main_loop():
    screen = video_init()
    x_wing = XWing(screen)
    stars = create_stars(screen)
    bullets = pygame.sprite.Group()
    enemy_bullets = pygame.sprite.Group()
    tie_fighters = pygame.sprite.Group()
    create_tie_fighters(screen, tie_fighters)

    while True:
        check_win(tie_fighters)
        create_enemy_bullets(screen, enemy_bullets)
        check_events(x_wing, bullets, screen)
        check_hit_tie_fighters(bullets, tie_fighters)
        check_hit_x_wing(enemy_bullets, x_wing)
        screen_update(screen, x_wing, bullets, tie_fighters, stars, enemy_bullets)


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
            new_bullet = XWingBullet(screen, x_wing)
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


def screen_update(screen, x_wing, bullets, tie_fighters, stars, enemy_bullets):
    x_wing.move()
    x_wing.update()
    bullets.update()
    enemy_bullets.update()
    tie_fighters.update()
    draw_bullets(bullets)
    draw_enemy_bullets(enemy_bullets)
    stars.update()
    pygame.display.update()
    screen.fill(color=s.SCREEN_COLOR)


def draw_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.y < 0:
            bullets.remove(bullet)
        else:
            bullet.draw()


def create_stars(screen):
    stars = pygame.sprite.Group()
    for _ in range(1000):
        star = Star(screen)
        stars.add(star)
    return stars


def create_tie_fighters(screen, tie_fighters):
    prototype = TieFighter(screen, 0, 0)
    for y in range(40, s.SCREEN_SIZE['height'] // 2, int(prototype.rect.height * 1.5)):
        for x in range(60, s.SCREEN_SIZE['width'] - 60, int(prototype.rect.width * 2.1)):
            tie_fighter = TieFighter(screen, x, y)
            tie_fighters.add(tie_fighter)


def check_hit_tie_fighters(bullets, tie_fighters):
    for tie_fighter in tie_fighters:
        for bullet in bullets:
            if tie_fighter.rect.y <= bullet.rect.y <= tie_fighter.rect.y + tie_fighter.rect.height:
                if tie_fighter.rect.x <= bullet.rect.x <= tie_fighter.rect.x + tie_fighter.rect.width:
                    tie_fighters.remove(tie_fighter)
                    bullets.remove(bullet)


def check_hit_x_wing(enemy_bullets, x_wing):
    for bullet in enemy_bullets:
        if x_wing.rect.y <= bullet.rect.y <= x_wing.rect.y + x_wing.rect.height:
            if x_wing.rect.x <= bullet.rect.x <= x_wing.rect.x + x_wing.rect.width:
                sys.exit()


def create_enemy_bullets(screen, enemy_bullets):
    if len(enemy_bullets) <= 5:
        enemy_bullet = TieFighterBullet(screen)
        enemy_bullets.add(enemy_bullet)


def draw_enemy_bullets(enemy_bullets):
    for bullet in enemy_bullets:
        if bullet.rect.y > s.SCREEN_SIZE['height']:
            enemy_bullets.remove(bullet)
        else:
            bullet.draw()


def check_win(tie_fighters):
    if len(tie_fighters) == 0:
        sys.exit()


if __name__ == '__main__':
    main_loop()
