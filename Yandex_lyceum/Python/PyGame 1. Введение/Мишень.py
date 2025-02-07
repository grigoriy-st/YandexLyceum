import pygame
import sys


pygame.init()
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


width = 500
height = 500


screen = pygame.display.set_mode((width, height))
        size = width, height = w * n * 2, w * n * 2
        if w <= 0 or n <= 0:
            raise ValueError

        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Шахматая доска")
        draw_circles(screen, w, n)
        pygame.display.flip()

pygame.display.set_caption("RGB мишень")


try:
    w, n = map(int, input("Введите толщину кольца и количество колец: ").split())
except ValueError:
    print("Неправильный формат ввода")
    sys.exit()


colors = [pygame.Color("red"), pygame.Color("green"), pygame.Color("blue")]


radius = w
x = 0
y = 0
for i in range(n):
    color = colors[i % 3]

    pygame.draw.circle(screen, color, (x + radius, y + radius), radius, w)
    radius += w


pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
