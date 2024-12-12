import pygame

def draw_board(screen, side_size, cell_quantity):
    w_cell = pygame.Color("white")
    b_cell = pygame.Color("black")
    cell_size = side_size // cell_quantity

    for row_c in range(side_size):
        for col_c in range(side_size):
            if (row_c + col_c) % 2 == 0:
                color = w_cell
            else:
                color = b_cell

            pygame.draw.rect(screen, color,
                             (
                                row_c * cell_size,
                                col_c * cell_size,
                                cell_size,
                                cell_size
                             )
                             )

if __name__ == '__main__':
    try:
        side_size, cell_quantity = list(map(int, input().split()))
        pygame.init()

        size = width, height = side_size, side_size
        if side_size <= 0 or cell_quantity <= 0:
            raise ValueError

        screen = pygame.display.set_mode(size)
        pygame.display.set_caption("Шахматая доска")
        draw_board(screen, side_size, cell_quantity)
        pygame.display.flip()

        while pygame.event.wait().type != pygame.QUIT:
            pass

    except ValueError:
        print("Неправильный формат ввода")
    finally:
        pygame.quit()
