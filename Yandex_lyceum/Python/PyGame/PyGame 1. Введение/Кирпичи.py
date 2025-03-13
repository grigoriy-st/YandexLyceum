import pygame
import math

def draw_rhomb(screen):
    for row in range(12):
        for col in range(10):
            x = col * (30 + 2)
            y = row * (15 + 2)
            if row % 2 == 1:
                x -= 15
            pygame.draw.rect(screen, "red", (x, y, 30, 15))


if __name__ == '__main__':
    try:
        pygame.init()
        size = (300, 200)

        screen = pygame.display.set_mode(size)
        screen.fill("white")

        pygame.display.set_caption("Кирпичи")
        draw_rhomb(screen)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()