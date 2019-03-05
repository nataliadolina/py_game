import pygame

pygame.init()
FPS = 50
clock = pygame.time.Clock()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)
running = True
flag = False
flag1 = False
x1, y1 = 0, 0
pygame.draw.rect(screen, (0, 255, 0), [x1, y1, 100, 100])
pygame.display.flip()
x, y = None, None
while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            flag = True
        elif event.type == pygame.MOUSEBUTTONUP:
            flag = False
        elif event.type == pygame.MOUSEMOTION:
            if flag:
                x, y = event.pos
    if x is not None and y is not None:
        if (x >= x1 and x <= x1 + 100) and (y >= y1 and y <= y1 + 100):
            delta_x, delta_y = x - x1, y - y1
            pygame.draw.rect(screen, (0, 255, 0), [x - delta_x, y + delta_y, 100, 100])
            x1, y1 = x, y
            flag1 = True
    if not flag1:
        pygame.draw.rect(screen, (0, 255, 0), [x1, y1, 100, 100])
    flag1 = False
    clock.tick(FPS)
    pygame.display.flip()
