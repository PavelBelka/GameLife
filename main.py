import pygame
from gameDisplay import GameDisplay

WIDTH = 360
HEIGHT = 480
FPS = 30
SCALE = 10

def main():
    running = True
    while running:
        #display.fill((0, 0, 0))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

def fill(screen_color, bcolor=[200, 200, 200]):
    """
    Заливает окно цветом
    :param screen_color: цвет окна
    :param bcolor: цвет границ
    """
    global screen
    surface = screen
    surface.fill(screen_color)
    w, h = surface.get_size()
    for i in range(0, w):
        pygame.draw.line(surface, bcolor, [i * SCALE, 0], [i * SCALE, h * SCALE])
    for i in range(0, h):
        pygame.draw.line(surface, bcolor, [0, i * SCALE], [w * SCALE, i * SCALE])


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
    main()