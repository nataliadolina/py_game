import pygame

pygame.init()
w = 800
h = 600
r = 0
FPS = 50
clock = pygame.time.Clock()
size = width, height = w, h
screen = pygame.display.set_mode(size)
running = True
p = None
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            p = event.pos
            r = 0
    if p is not None:
        r += 100 // FPS
        pygame.draw.circle(screen, pygame.Color('Yellow'), p, r)
    clock.tick(FPS)
    pygame.display.flip()
