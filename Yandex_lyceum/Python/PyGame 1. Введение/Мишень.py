import pygame
import sys


pygame.init()


width = 500
height = 500


screen = pygame.display.set_mode((width, height))


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