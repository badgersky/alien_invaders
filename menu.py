import sys
import pygame as p
import settings as s
from empire_invaders import EmpireInvaders
from star import Star
from text import Text


class Menu:

    def __init__(self, title_img):
        p.init()
        self.screen = p.display.set_mode((1080, 720))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        p.display.set_caption('Empire Invaders')
        self.stars = p.sprite.Group()

        play_button_img = p.image.load('images/play_button.bmp')
        quit_button_img = p.image.load('images/quit_button.bmp')

        self.title = Text(self.screen, title_img, self.width // 2, self.height // 4)
        self.quit_button = Text(self.screen, quit_button_img, self.width // 2, self.height // 1.3)
        self.play_button = Text(self.screen, play_button_img, self.width // 2, self.height // 1.7)

    def main_loop(self):
        self.create_stars()
        while True:
            self.check_events()
            self.screen.fill(color=s.SCREEN_COLOR)
            self.stars.update()
            self.quit_button.blit_text()
            self.play_button.blit_text()
            self.title.blit_text()
            p.display.flip()

    def check_events(self):
        for event in p.event.get():
            if event.type == p.QUIT:
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                mouse_pos = p.mouse.get_pos()
                if self.quit_button.rect.collidepoint(mouse_pos):
                    sys.exit()
                if self.play_button.rect.collidepoint(mouse_pos):
                    game = EmpireInvaders()
                    game.main_loop()

    def create_stars(self):
        for _ in range(500):
            new_star = Star(self.screen)
            self.stars.add(new_star)


class MainMenu(Menu):

    def __init__(self):
        title_img = p.image.load('images/title.bmp')
        super().__init__(title_img)

    def main_loop(self):
        super().main_loop()


class LoseMenu(Menu):
    pass


class WinMenu(Menu):
    pass


if __name__ == '__main__':
    menu = MainMenu()
    menu.main_loop()
