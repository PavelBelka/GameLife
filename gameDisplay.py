import pygame

EDGE_WIDTH = 20
START_POSX = 20
START_POSY = 20
LINE_WIDTH = 2
AGENT_WIDTH = 4

class GameDisplay:
    def __init__(self, width = 640, height = 480, cell_size = 10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color('white'))

        self.cell_width = (self.width - 2 * EDGE_WIDTH) // self.cell_size
        self.cell_height = (self.height - 2 * EDGE_WIDTH) // self.cell_size

    def draw_cell(self, a_matrix, f_matrix):
        self.screen.fill(pygame.Color('white'))
        for i in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('gray66'), [START_POSX, START_POSY + i],
                             [self.width - START_POSX, START_POSY + i], LINE_WIDTH)
        for i in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('gray66'), [START_POSX + i, START_POSY],
                             [START_POSX + i, self.height - START_POSY], LINE_WIDTH)
        for i in range(0, self.cell_height):
            for j in range(0, self.cell_width):
                if f_matrix[i][j] > 10:
                    pygame.draw.rect(self.screen, pygame.Color('green2'),
                                     [START_POSX + self.cell_size * j + LINE_WIDTH,
                                      START_POSY + self.cell_size * i + LINE_WIDTH,
                                      self.cell_size - LINE_WIDTH, self.cell_size - LINE_WIDTH])
                elif 0 < f_matrix[i][j] <= 10:
                    pygame.draw.rect(self.screen, pygame.Color('green4'),
                                     [START_POSX + self.cell_size * j + LINE_WIDTH,
                                      START_POSY + self.cell_size * i + LINE_WIDTH,
                                      self.cell_size - LINE_WIDTH, self.cell_size - LINE_WIDTH])
                else:
                    pygame.draw.rect(self.screen, pygame.Color('black'),
                                     [START_POSX + self.cell_size * j + LINE_WIDTH,
                                      START_POSY + self.cell_size * i + LINE_WIDTH,
                                      self.cell_size - LINE_WIDTH, self.cell_size - LINE_WIDTH])
                if a_matrix[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('red'),
                                     [START_POSX + self.cell_size * j + LINE_WIDTH + AGENT_WIDTH,
                                      START_POSY + self.cell_size * i + LINE_WIDTH + AGENT_WIDTH,
                                      self.cell_size - LINE_WIDTH - AGENT_WIDTH * 2, self.cell_size - LINE_WIDTH - AGENT_WIDTH * 2])




