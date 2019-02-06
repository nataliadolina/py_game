import pygame


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.coords = []
        self.b = []
        self.k3 = 0

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        arr = []
        for i in range(self.height):
            for j in range(self.width):
                r = pygame.draw.rect(screen, (255, 255, 255),
                                     [self.top + self.cell_size * j, self.left + self.cell_size * i, self.cell_size,
                                      self.cell_size], 1)
                self.coords.append((j, i))
                arr.append(r)
            self.b.append(arr)
            arr = []

    def sizes(self):
        return self.left, self.top, self.cell_size

    def update(self, k1, k2, pos):
        for i in range(self.height):
            for j in range(self.width):
                if j == k1 and i != k2 or j != k1 and i == k2:
                    if screen.get_at((self.left + self.cell_size * j, self.top + self.cell_size * i)) == (0, 0, 0):
                        pygame.draw.rect(screen, (255, 255, 255),
                                         [self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size,
                                          self.cell_size])
                    elif screen.get_at((self.left + self.cell_size * j - int(0.5 * self.cell_size),
                                        self.top + self.cell_size * i - int(0.5 * self.cell_size))) == (255, 255, 255):
                        pygame.draw.rect(screen, (255, 255, 255),
                                         [self.left + self.cell_size * j, self.top + self.cell_size * i, self.cell_size,
                                          self.cell_size], 1)
        if screen.get_at(pos) == (0, 0, 0):
            pygame.draw.rect(screen, (255, 255, 255),
                             [self.left + self.cell_size * k1, self.top + self.cell_size * k2, self.cell_size,
                              self.cell_size])
        elif screen.get_at(pos) == (255, 255, 255):
            pygame.draw.rect(screen, (255, 255, 255),
                             [self.left + self.cell_size * k1, self.top + self.cell_size * k2, self.cell_size,
                              self.cell_size], 1)


pygame.init()
x, y = 300, 300
size = width, height = x, y
screen = pygame.display.set_mode(size)
running = True
ex = Board(5, 7)
ex.set_view(30, 30, 30)
ex.render()
pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos_x, pos_y = event.pos
            l_x, l_y, cell_size = ex.sizes()
            n1 = (pos_x - l_x) // cell_size
            n2 = (pos_y - l_y) // cell_size
            ex.update(n1, n2, (pos_x, pos_y))
    pygame.display.flip()
