import pygame as p


class Explosion(p.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.images = [p.image.load(f'images/exp{i}.png') for i in range(1, 6)]
        self.index = 0
        self.counter = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        animation_speed = 8
        self.counter += 1
        if self.counter >= animation_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= animation_speed:
            self.kill()


if __name__ == '__main__':
    pass