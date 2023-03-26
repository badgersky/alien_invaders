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
            self.check_win()
            self.check_events()
            self.check_hit_tie_fighters()
            self.check_hit_x_wing()
            self.stars.update()
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
        self.spaceship.update()
        self.tie_fighters.update()
        self.bullets.update()
        self.enemy_bullets.update()
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
        if len(self.enemy_bullets) <= 10:
            for _ in range(2):
                enemy_bullet = TieFighterBullet(self.screen)
                self.enemy_bullets.add(enemy_bullet)

    def draw_bullets(self):
        for bullet in self.bullets:
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
            else:
                bullet.draw()
        for bullet in self.enemy_bullets:
            if bullet.rect.y > s.SCREEN_SIZE['height']:
                self.enemy_bullets.remove(bullet)
            else:
                bullet.draw()

    def create_tie_fighters(self):
        prototype = TieFighter(self.screen, 0, 0)
        for y in range(40, s.SCREEN_SIZE['height'] // 2, int(prototype.rect.height * 1.5)):
            for x in range(60, s.SCREEN_SIZE['width'] - 60, int(prototype.rect.width * 2.1)):
                tie_fighter = TieFighter(self.screen, x, y)
                self.tie_fighters.add(tie_fighter)

    def check_hit_tie_fighters(self):
        for tie_fighter in self.tie_fighters:
            for bullet in self.bullets:
                if tie_fighter.rect.y <= bullet.rect.y <= tie_fighter.rect.y + tie_fighter.rect.height:
                    if tie_fighter.rect.x <= bullet.rect.x <= tie_fighter.rect.x + tie_fighter.rect.width:
                        self.tie_fighters.remove(tie_fighter)
                        self.bullets.remove(bullet)

    def check_hit_x_wing(self):
        for bullet in self.enemy_bullets:
            if self.spaceship.rect.y <= bullet.rect.y <= self.spaceship.rect.y + self.spaceship.rect.height:
                if self.spaceship.rect.x <= bullet.rect.x <= self.spaceship.rect.x + self.spaceship.rect.width:
                    sys.exit()

    def check_win(self):
        if len(self.tie_fighters) == 0:
            sys.exit()


if __name__ == '__main__':
    empire_invaders = EmpireInvaders()
    empire_invaders.main_loop()
