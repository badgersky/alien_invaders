import sys
import pygame as p
import settings as s
from empire_invaders import EmpireInvaders
from star import Star


class MainMenu:

    def __init__(self):
        self.screen = p.display.set_mode((1080, 720))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        p.display.set_caption('Empire Menu')
        self.stars = p.sprite.Group()

    def main_loop(self):
        self.create_stars()
        while True:
            self.check_events()
            self.screen.fill(color=s.SCREEN_COLOR)
            self.stars.update()
            p.display.flip()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
            if event.type == p.KEYDOWN:
                if event.key == p.K_ESCAPE:
                    sys.exit()

    def create_stars(self):
        for _ in range(500):
            new_star = Star(self.screen)
            self.stars.add(new_star)

    def button_play_pressed(self):
        return True


if __name__ == '__main__':
    menu = MainMenu()
    menu.main_loop()
