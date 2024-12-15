import random
import pygame
from PyQt5.QtWidgets.QScroller import velocity

v = 10
is_created_ball = False
circle_color = pygame.Color('yellow')

if __name__ == '__main__':
    try:
        pygame.init()
        size = width, height = random.randint(200, 400), random.randint(200, 400)

        screen = pygame.display.set_mode(size)
        balls = []
        velocities = []
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = event.pos
                    balls.append(list(pos))
                    velocities.append()
                    is_created_ball = True



            if is_created_ball:

                # if pos > (width, height):
                #     pos = pos[0] - 1, pos[1] - 1
                # if pos < (width, height):
                #     pos = pos[0] + 1, pos[1] + 1

                if pos[0] > width:
                    pos = pos[0] + 1, pos[1] - 1
                if pos[1] > height:
                    pos = pos[0] - 1, pos[1] + 1

                pygame.draw.circle(screen, (pygame.Color('white')), pos, 10, 0)
                pos = pos[0] - 1, pos[1] - 1


            pygame.display.flip()


    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()