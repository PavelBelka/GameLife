import pygame
import numpy as np
from gameDisplay import GameDisplay

WIDTH = 360
HEIGHT = 480
FPS = 30
SCALE = 10

def main(disp):
    running = True
    zero = get_list(disp.cell_width, disp.cell_height)
    print(zero)
    disp.draw_cell(zero)
    pygame.display.flip()
    while running:
        #display.fill((0, 0, 0))

        #pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

def get_list(width, height):
    np.random.seed(1234)
    data = np.random.randint(0, 2, (height, width))
    return data

def draw_point(surface, color, pos):
    """
    Закрашивает клеточку
    :param surface: поверхность (окно, например)
    :param color: цвет
    :param pos: координаты клетки
    """
    return pygame.draw.rect(surface, color, [pos[0] * SCALE, pos[1] * SCALE,  SCALE, SCALE])

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = GameDisplay(640, 480 , 20)
    screen.draw_grid()
    clock.tick(FPS)
    main(screen)