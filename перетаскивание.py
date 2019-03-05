import pygame

pygame.init()
FPS = 50
clock = pygame.time.Clock()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
running = True
flag = False
p = None
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = True
        elif event.type == pygame.MOUSEBUTTONUP:
            flag = False
        elif event.type == pygame.MOUSEMOTION:
            pos = event.pos
