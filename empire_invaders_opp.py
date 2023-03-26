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
        p.display.set_caption('Empire Invaders')

    def main_loop(self):
        while True:
            for event in p.event.get():
                if event.type == p.QUIT:
                    sys.exit()
                if event.type == p.KEYDOWN:
                    if event.key == p.K_ESCAPE:
                        sys.exit()

            self.screen.fill(color=s.SCREEN_COLOR)
            p.display.flip()


if __name__ == '__main__':
    empire_invaders = EmpireInvaders()
    empire_invaders.main_loop()