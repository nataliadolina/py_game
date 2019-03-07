import pygame
import os
from random import randrange

pygame.init()
x, y = 500, 500
size = width, height = x, y
screen = pygame.display.set_mode(size)
screen.fill((0, 0, 0))


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb2.png")
    image_boom = load_image("boom.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.img = Bomb.image_boom
        self.rect = self.image.get_rect()

    def coords(self):
        x, y = randrange(0, 401), randrange(0, 400)
        self.rect = self.rect.move(x, y)
        all_sprites.remove(self)
        while pygame.sprite.spritecollideany(self, all_sprites):
            x, y = randrange(400), randrange(399)
            self.rect = self.rect.move(x, y)
        all_sprites.add(self)

    def get_event(self, event):
        if self.rect.collidepoint(event.pos):
            c = self.rect.center
            self.image = self.img
            self.rect = self.image.get_rect()
            self.rect.center = c


x, y = 0, 0
running = True
screen.fill((255, 255, 255))
all_sprites = pygame.sprite.Group()
for i in range(10):
    Bomb(all_sprites)
for i in all_sprites:
    i.coords()
while running:
    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    all_sprites.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            for i in all_sprites:
                i.get_event(event)
    pygame.display.flip()
