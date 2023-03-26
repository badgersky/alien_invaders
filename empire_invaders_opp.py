import pygame as p
import sys
import settings as s
from bullet import XWingBullet, TieFighterBullet
from spaceship import XWing, TieFighter
from star import Star


class EmpireInvaders:

    def __init__(self):
        p.init()

        self.screen = p.display.set_mode((0, 0), p.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        s.SCREEN_SIZE['width'], s.SCREEN_SIZE['height'] = self.screen_width, self.screen_height
        p.display.set_caption('Empire Invaders')

        self.spaceship = XWing(self.screen)
        self.tie_fighters = p.sprite.Group()

        self.stars = p.sprite.Group()

        self.bullets = p.sprite.Group()
        self.enemy_bullets = p.sprite.Group()

    def main_loop(self):
        self.create_stars()
        self.create_tie_fighters()
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
            if event.type == p.KEYDOWN:
                self.check_keydown_events(event)
            if event.type == p.KEYUP:
                self.check_keyup_events(event)

    def check_keyup_events(self, event):
        if event.key == p.K_LEFT:
            self.spaceship.moving_left = False
        if event.key == p.K_RIGHT:
            self.spaceship.moving_right = False

    def check_keydown_events(self, event):
        if event.key == p.K_ESCAPE:
            sys.exit()
        if event.key == p.K_SPACE:
            self.create_bullets()
        if event.key == p.K_LEFT:
            self.spaceship.moving_left = True
        if event.key == p.K_RIGHT:
            self.spaceship.moving_right = True

    def update_screen(self):
        self.stars.update()
        self.spaceship.move()
        self.spaceship.update()
        self.tie_fighters.update()
        self.bullets.update()
        self.draw_bullets()
        p.display.flip()
        self.screen.fill(color=s.SCREEN_COLOR)

    def create_stars(self):
        for _ in range(1000):
            star = Star(self.screen)
            self.stars.add(star)

    def create_bullets(self):
        if len(self.bullets) < 5:
            new_bullet = XWingBullet(self.screen, self.spaceship)
            self.bullets.add(new_bullet)

    def draw_bullets(self):
        for bullet in self.bullets:
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
            else:
                bullet.draw()

    def create_tie_fighters(self):
        prototype = TieFighter(self.screen, 0, 0)
        for y in range(40, s.SCREEN_SIZE['height'] // 2, int(prototype.rect.height * 1.5)):
            for x in range(60, s.SCREEN_SIZE['width'] - 60, int(prototype.rect.width * 2.1)):
                tie_fighter = TieFighter(self.screen, x, y)
                self.tie_fighters.add(tie_fighter)


if __name__ == '__main__':
    empire_invaders = EmpireInvaders()
    empire_invaders.main_loop()
