import pygame
import math

def draw_rhomb(screen, side_length):
    info = pygame.display.Info()
    max_width = info.current_w
    max_height = info.current_h

    max_rombs_in_w = max_width // n
    max_rombs_in_h = max_height // n
    for row_r in range(max_rombs_in_h):
        for col_r in range(max_rombs_in_w):
            x = col_r * side_length + side_length // 2
            y = row_r * side_length + side_length // 2
            diamond_points = [
                (x, y - side_length // 2),
                (x + side_length // 2, y),
                (x, y + side_length // 2),
                (x - side_length // 2, y)
            ]
            pygame.draw.polygon(screen, "orange", diamond_points)


if __name__ == '__main__':
    try:
        n = int(input())
        pygame.init()

        size = (300, 300)
        if n <= 0:
            raise ValueError

        screen = pygame.display.set_mode(size)
        screen.fill("yellow")

        pygame.display.set_caption("Ромбики")
        draw_rhomb(screen, n)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()