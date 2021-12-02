import pygame

class GameDisplay:
    def __init__(self, width = 640, height = 480, cell_size = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color('white'))

        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

    def draw_grid(self):
        for i in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), [i, 0], [i, self.height])
        for i in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), [0, i], [self.width, i])
        pygame.display.flip()

    def draw_cell(self, matrix):
        for i in range(0, self.cell_height):
            for j in range(0, self.cell_width):
                if matrix[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (self.cell_size * j, self.cell_size * i,
                                                                          self.cell_size, self.cell_size))




