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


arr = []


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb2.png")
    image_boom = load_image("boom.png")

    def __init__(self, group):
        super().__init__(group)
        self.image = Bomb.image
        self.img = Bomb.image_boom
        self.rect = self.image.get_rect()

    def peresek(self, x, y):
        x1, y1, a1, b1 = self.rect.x, self.rect.y, 100, 101
        x2, y2, a2, b2 = x, y, 100, 101
        x_0, y_0 = x1, y1
        x_1, y_1 = x1 + a1, y1 + b1
        x_2, y_2 = x2, y2
        x_3, y_3 = x2 + a2, y2 + b2
        if x_0 > x_3 or x_1 < x_2 or y_0 > y_3 or y_1 < y_2:
            return False
        else:
            return True

    def coords(self):
        self.rect.x = randrange(400)
        self.rect.y = randrange(399)
        for i in arr:
            x0, y0 = i
            while self.peresek(x0, y0):
                self.rect.x = randrange(400)
                self.rect.y = randrange(399)
        arr.append((self.rect.x, self.rect.y))

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
            print(arr)
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            for i in all_sprites:
                i.get_event(event)
    pygame.display.flip()

