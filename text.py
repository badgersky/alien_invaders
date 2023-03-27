class Text:

    def __init__(self, screen, image, x, y):
        self.image = image
        self.screen = screen

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def blit_text(self):
        self.screen.blit(self.image, self.rect)


if __name__ == '__main__':
    pass

