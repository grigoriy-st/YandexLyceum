import pygame

def draw_square(screen, width, height):
    color = pygame.Color(255, 0, 0)

    pygame.draw.rect(screen, color,
                     (1, 1, width - 3, height - 3), 0)


if __name__ == '__main__':
    try:
        width, height = list(map(int, input().split()))
        if width <= 0 or height <= 0:
            raise ValueError
        elif width == height:
            raise ValueError

        pygame.init()

        size = width, height = width, height
        if width <= 0 or height <= 0:
            raise ValueError

        screen = pygame.display.set_mode(size)

        draw_square(screen, width, height)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()
