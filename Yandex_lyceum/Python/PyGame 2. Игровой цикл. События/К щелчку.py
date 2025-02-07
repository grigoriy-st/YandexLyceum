import pygame

def main():
    try:
        pygame.init()
        size = width, height = 500, 500

        screen = pygame.display.set_mode(size)
        running = True
        is_pressed = False

        speed = 0.007
        circle_pos = [width // 2, height // 2]
        circle_r = 20
        target_pos = circle_pos.copy()


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    target_pos = list(event.pos)
                
            d1 = target_pos[0] - circle_pos[0]
            d2 = target_pos[1] - circle_pos[1]

            circle_pos[0] += d1 * speed
            circle_pos[1] += d2 * speed

            if abs(d1) < 1 and abs(d2) < 1:
                circle_pos[0] = target_pos[0]
                circle_pos[1] = target_pos[1]

            
            screen.fill("black")
            pygame.draw.circle(screen, "red", tuple(circle_pos), circle_r)
            pygame.display.flip()

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()