import pygame
import settings as s
from random import randint


class Star(pygame.sprite.Sprite):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.color = s.STAR_COLOR

        screen_width = s.SCREEN_SIZE['width']
        screen_height = s.SCREEN_SIZE['height']
        width = s.STAR_SIZE['width']
        height = s.STAR_SIZE['height']
        position_x = randint(0, screen_width)
        position_y = randint(0, screen_height)
        self.rect = pygame.Rect((position_x, position_y), (width, height))

    def draw_star(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


if __name__ == '__main__':
    pass
