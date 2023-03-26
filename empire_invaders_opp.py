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
        while True:
            self.check_events()
            self.update_screen()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    sys.exit()

    def update_screen(self):
        self.spaceship.update()
        self.stars.update()
        p.display.flip()

    def create_stars(self):
        for _ in range(1000):
            star = Star(self.screen)
            self.stars.add(star)


if __name__ == '__main__':
    empire_invaders = EmpireInvaders()
    empire_invaders.main_loop()
