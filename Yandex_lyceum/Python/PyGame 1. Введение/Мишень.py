import pygame

colors_list = ['red', "blue", "green"]

def draw_circles(screen, width, n):
    id_c = 0
    center_coords = (width * n, width * n)
    radius = 30
    pygame.draw.circle(screen, "red", center_coords, radius)

    for circle in range(n, 0, -1):
        pygame.draw.circle(screen,
                           colors_list[id_c % 3],
                           center_coords, w * circle)
        id_c += 1
    ...


if __name__ == '__main__':
    try:
        w, n = list(map(int, input().split()))
        pygame.init()

        size = width, height = w * n * 2, w * n * 2
        if w <= 0 or n <= 0:
            raise ValueError

        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Шахматая доска")
        draw_circles(screen, w, n)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()
