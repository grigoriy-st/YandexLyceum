import pygame

def draw_cross(screen, width, height):
    line_color = pygame.Color("white")

    pygame.draw.line(screen, line_color, (0, 0), (width, height), 5)
    pygame.draw.line(screen, line_color, (width, 0), (0, height), 5)

if __name__ == '__main__':
    try:
        width, height = list(map(int, input().split()))
        pygame.init()

        size = width, height = width, height
        if width <= 0 or height <= 0:
            raise ValueError

        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Крест")
        draw_cross(screen, width, height)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()
