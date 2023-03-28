import pygame as p
import sys
import settings as s
from bullet import XWingBullet, TieFighterBullet
from menu import MainMenu, LoseMenu, WinMenu, PauseMenu
from spaceship import XWing, TieFighter
from star import Star
from explosion import Explosion
import time


class EmpireInvaders:

    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((0, 0), p.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        s.SCREEN_SIZE['width'], s.SCREEN_SIZE['height'] = self.screen_width, self.screen_height
        p.display.set_caption('Empire Invaders')

        self.spaceship = XWing(self.screen)

        self.tie_fighters, self.bullets, self.enemy_bullets, self.stars, self.explosions = self.create_sprites()

        self.pause_menu = PauseMenu(self)

        self.menu = MainMenu(self)
        self.menu.main_loop()

    @ staticmethod
    def create_sprites():
        tie_fighters = p.sprite.Group()
        bullets = p.sprite.Group()
        enemy_bullets = p.sprite.Group()
        stars = p.sprite.Group()
        explosions = p.sprite.Group()
        return tie_fighters, bullets, enemy_bullets, stars, explosions

    def main_loop(self):
        p.mouse.set_visible(False)
        if len(self.tie_fighters) == 0:
            self.create_tie_fighters()
        if len(self.stars) == 0:
            self.create_stars()
        while True:
            self.check_win()
            self.check_lose()
            self.check_events()
            self.check_hit_tie_fighters()
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
            p.mouse.set_visible(True)
            self.pause_menu.main_loop()
        if event.key == p.K_SPACE:
            self.create_bullets()
        if event.key == p.K_LEFT:
            self.spaceship.moving_left = True
        if event.key == p.K_RIGHT:
            self.spaceship.moving_right = True

    def update_screen(self):
        self.spaceship.update()
        self.bullets.update()
        self.enemy_bullets.update()
        self.draw_bullets()
        self.tie_fighters.update()
        self.explosions.update()
        self.explosions.draw(self.screen)
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
        if len(self.enemy_bullets) <= 15:
            for _ in range(3):
                enemy_bullet = TieFighterBullet(self.screen)
                self.enemy_bullets.add(enemy_bullet)

    def draw_bullets(self):
        for bullet in self.bullets:
            if bullet.rect.y < 0:
                self.bullets.remove(bullet)
            else:
                bullet.draw()
        for bullet in self.enemy_bullets:
            if bullet.rect.y > self.screen_height:
                self.enemy_bullets.remove(bullet)
            else:
                bullet.draw()

    def create_tie_fighters(self):
        prototype = TieFighter(self.screen, 0, 0)
        for y in range(40, self.screen_height // 2, int(prototype.rect.height * 1.5)):
            for x in range(60, self.screen_width - 60, int(prototype.rect.width * 2.1)):
                tie_fighter = TieFighter(self.screen, x, y)
                self.tie_fighters.add(tie_fighter)

    def check_hit_tie_fighters(self):
        for tie_fighter in self.tie_fighters:
            for bullet in self.bullets:
                if tie_fighter.rect.collidepoint(bullet.rect.x, bullet.rect.y):
                    self.bullets.remove(bullet)
                    x, y = tie_fighter.rect.center
                    self.tie_fighters.remove(tie_fighter)
                    explosion = Explosion(x, y)
                    self.explosions.add(explosion)

    def check_lose(self):
        for bullet in self.enemy_bullets:
            if self.spaceship.rect.collidepoint(bullet.rect.x, bullet.rect.y):
                # resetting game properties
                self.tie_fighters, self.bullets, self.enemy_bullets, self.stars, self.explosions = self.create_sprites()
                self.spaceship = XWing(self.screen)
                p.time.wait(500)
                p.mouse.set_visible(True)
                lose_screen = LoseMenu(self)
                lose_screen.main_loop()

    def check_win(self):
        if len(self.tie_fighters) == 0:
            # resetting game properties
            self.tie_fighters, self.bullets, self.enemy_bullets, self.stars, self.explosions = self.create_sprites()
            self.spaceship = XWing(self.screen)
            p.time.wait(500)
            p.mouse.set_visible(True)
            win_screen = WinMenu(self)
            win_screen.main_loop()


if __name__ == '__main__':
    empire_invaders = EmpireInvaders()
