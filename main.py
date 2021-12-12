import pygame
from gameDisplay import GameDisplay
from world import World

WIDTH = 360
HEIGHT = 480
FPS = 4

def main(disp):
    running = True
    start_world = World(disp.cell_width, disp.cell_height, 100, 10122021)
    print(start_world.get_agents_matrix())
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        disp.draw_cell(start_world.get_agents_matrix(), start_world.get_food_matrix())
        pygame.display.flip()
        start_world.rule()
        start_world.update()
        clock.tick(FPS)
    pygame.quit()

if __name__ == '__main__':
    pygame.init()
    clock = pygame.time.Clock()
    screen = GameDisplay(640, 480 , 20)
    main(screen)