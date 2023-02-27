import pygame
import sys
import settings as s


def video_init():
    pygame.init()
    width = s.SCREEN_SIZE['width']
    height = s.SCREEN_SIZE['height']
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Alien Invaders')
    return screen


def main_loop():
    screen = video_init()

    while True:
        check_events()

        blit_spaceship(screen)
        pygame.display.flip()
        screen.fill(color=s.SCREEN_COLOR)


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def load_spaceship():
    image = pygame.image.load('images/spaceship.bmp')
    spaceship = image.get_rect()
    return image, spaceship


def blit_spaceship(screen):
    image, spaceship = load_spaceship()
    screen_rect = screen.get_rect()
    spaceship.midbottom = screen_rect.midbottom
    screen.blit(image, spaceship)
    

if __name__ == '__main__':
    main_loop()
