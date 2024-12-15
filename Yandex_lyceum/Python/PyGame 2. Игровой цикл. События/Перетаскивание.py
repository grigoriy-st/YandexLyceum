import pygame

if __name__ == '__main__':
    try:
        pygame.init()
        size = width, height = 300, 300

        screen = pygame.display.set_mode(size)
        running = True
        is_pressed = False

        square_pos = [0, 0]
        square_size = 100

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    m_pos = event.pos
                    square_rect = pygame.Rect(square_pos[0], square_pos[1], square_size, square_size)

                    if square_rect.collidepoint(m_pos):
                        is_pressed = True
                        move_to_x = square_pos[0] - m_pos[0]
                        move_to_y = square_pos[1] - m_pos[1]

                if event.type == pygame.MOUSEBUTTONUP:
                    is_pressed = False

                if event.type == pygame.MOUSEMOTION:
                    if is_pressed:
                        square_pos[0] = event.pos[0] + move_to_x
                        square_pos[1] = event.pos[1] + move_to_y

            screen.fill("black")
            square_rect = pygame.draw.rect(screen, "green", (square_pos[0], square_pos[1], square_size, square_size))
            pygame.display.flip()

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()