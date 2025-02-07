import math
import pygame

a = b = 70
angle = math.radians(30)
osnovanie = math.sqrt((a ** 2 + b ** 2) - (2 * a * b * math.cos(angle)))

class Fan:
    def __init__(self):
        self.top_fan_blade = [(101, 101), (101 + osnovanie / 2, 101 - a), (101 - osnovanie / 2, 101 - a)]
        self.right_fan_blade =  [(101, 101), (171, 121), ((101 + osnovanie / 2) + 35, 150)]
        self.left_fan_blade = [(101, 101), (101 - 70, 121), ((101 - osnovanie / 2) - 35, 150)]

def main():
    pygame.init()

    clock = pygame.time.Clock()
    size = width, height = 210, 210
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Вентилятор")

    fan = Fan()
    pygame.draw.polygon(screen, "white", fan.top_fan_blade)
    pygame.draw.polygon(screen, "white", fan.right_fan_blade)
    pygame.draw.polygon(screen, "white", fan.left_fan_blade)

    rotation_speed = 0
    angle = 0
    is_running = True

    while is_running:
        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    rotation_speed -= 1
                if event.button == 3:
                    rotation_speed += 1
            
            if event.type == pygame.MOUSEBUTTONUP:
                ...
        
        angle += rotation_speed
        rotated_surface = pygame.transform.rotate(screen, angle)
        rect = rotated_surface.get_rect(center=(101, 101))
        screen.blit(rotated_surface, rect)

        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()