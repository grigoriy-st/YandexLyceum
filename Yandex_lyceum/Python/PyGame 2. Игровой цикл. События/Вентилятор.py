import pygame


class Fan:
    def __init__(self):
        """ Доделать эти значения"""
        self.top_fan_blade = [(80, 30), (]
        self.left_fan_blade = [(105, 105), (40, 160), (30, 110)]
        self.right_fan_blade = [(105, 105), (170, 150), (150, 190)]

    def rotate_clockwise(screen):
        """ Вращение вентиятора по часовой стрелке. """
        ...

    def rotate_counterclockwise(screen):
        """ Вращение вентилятора против часовой стрелки. """


if __name__ == "__main__":
    size = width, height = 201, 201
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Вентилятор")
    is_running = True

    fan = Fan()
    
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print("LKM")
                if event.button == 3:
                    print("RKM")

        pygame.draw.circle(screen, "white",
                           center=(210 // 2, 210 // 2), radius=10)
        
        pygame.draw.polygon(screen, "white", fan.left_fan_blade, 0)
        pygame.draw.polygon(screen, "white", fan.right_fan_blade, 0)
        pygame.draw.polygon(screen, "white", fan.top_fan_blade, 0)

        pygame.display.flip()

pygame.quit()

