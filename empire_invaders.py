import random
import pygame as p
import sys

import settings as s
from bullet import XWingBullet, TieFighterBullet
from menu import MainMenu, LoseMenu, WinMenu, PauseMenu
from spaceship import XWing, TieFighter
from star import Star
from explosion import Explosion


class EmpireInvaders:

    def __init__(self):
        p.init()
        self.screen = p.display.set_mode((0, 0), p.FULLSCREEN)
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        s.SCREEN_SIZE['width'], s.SCREEN_SIZE['height'] = self.screen_width, self.screen_height
        p.display.set_caption('Empire Invaders')

        self.x_wing_img = 'images/x-wing.bmp'
        self.tie_fight_img = 'images/tie_fighter.bmp'

        self.spaceship = XWing(self.screen, self.x_wing_img)
        self.tie_fighters, self.bullets, self.enemy_bullets, self.stars, self.explosions = self.create_sprites()

        self.laser_sound = p.mixer.Sound('sounds/laser.wav')
        self.explosion_sound = p.mixer.Sound('sounds/boom.wav')
        self.laser_sound.set_volume(0.4)
        self.explosion_sound.set_volume(0.4)

        self.level = 1
        self.score = 0
        self.font = p.font.Font('fonts/slkscr.ttf', 30)

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
        p.mixer.music.load('sounds/main_theme.mp3')
        p.mixer.music.set_volume(0.1)
        p.mixer.music.play(-1)
        p.mouse.set_visible(False)
        if len(self.tie_fighters) == 0:
            self.create_tie_fighters()
        if len(self.stars) == 0:
            self.create_stars()
        while True:
            self.create_enemy_bullets()
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
        self.draw_score()
        self.draw_level()
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
        if len(self.bullets) < 3:
            self.laser_sound.play()
            new_bullet = XWingBullet(self.screen, self.spaceship)
            self.bullets.add(new_bullet)

    def create_enemy_bullets(self):
        limit = 5 * self.level
        if len(self.enemy_bullets) < 5:
            self.laser_sound.set_volume(0.02)
            self.laser_sound.play()
            self.laser_sound.set_volume(0.4)
            for _ in range(limit):
                new_bullet = TieFighterBullet(self.screen, random.choice(list(self.tie_fighters)))
                self.enemy_bullets.add(new_bullet)

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

    def draw_score(self):
        color = (250, 253, 15)
        img = self.font.render(f'Score: {self.score}', True, color)
        self.screen.blit(img, (10, self.screen_height - 40))

    def draw_level(self):
        color = (250, 253, 15)
        img = self.font.render(f'level: {self.level}', True, color)
        self.screen.blit(img, (self.screen_width - 170, self.screen_height - 40))

    def create_tie_fighters(self):
        prototype = TieFighter(self.screen, 0, 0, self.tie_fight_img)
        for y in range(40, self.screen_height // 2, int(prototype.rect.height * 1.5)):
            for x in range(60, self.screen_width - 60, int(prototype.rect.width * 2.1)):
                tie_fighter = TieFighter(self.screen, x, y, self.tie_fight_img)
                self.tie_fighters.add(tie_fighter)

    def check_hit_tie_fighters(self):
        for tie_fighter in self.tie_fighters:
            for bullet in self.bullets:
                if tie_fighter.rect.collidepoint(bullet.rect.x, bullet.rect.y):
                    self.score += 10
                    self.explosion_sound.play()
                    self.bullets.remove(bullet)
                    x, y = tie_fighter.rect.center
                    self.tie_fighters.remove(tie_fighter)
                    explosion = Explosion(x, y)
                    self.explosions.add(explosion)

    def check_lose(self):
        for bullet in self.enemy_bullets:
            if self.spaceship.rect.collidepoint(bullet.rect.x, bullet.rect.y):
                self.explosion_sound.play()
                # resetting game properties
                self.tie_fighters, self.bullets, self.enemy_bullets, self.stars, self.explosions = self.create_sprites()
                self.spaceship = XWing(self.screen, self.x_wing_img)
                self.score = 0
                p.time.wait(500)
                p.mouse.set_visible(True)
                lose_screen = LoseMenu(self)
                lose_screen.main_loop()

    def check_win(self):
        if len(self.tie_fighters) == 0:
            if self.level == 5:
                p.time.wait(500)
                p.mouse.set_visible(True)
                win_screen = WinMenu(self)
                win_screen.main_loop()
            else:
                # resetting game properties
                self.tie_fighters, self.bullets, self.enemy_bullets, self.stars, self.explosions = self.create_sprites()
                self.spaceship = XWing(self.screen, self.x_wing_img)
                self.level += 1
                self.main_loop()


if __name__ == '__main__':
    empire_invaders = EmpireInvaders()
