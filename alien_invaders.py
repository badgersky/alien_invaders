import pygame
import sys


def video_init():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption('Alien Invaders')
    return screen


def main_loop():
    video_init()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        pygame.display.flip()


if __name__ == '__main__':
    main_loop()