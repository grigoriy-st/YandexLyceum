import pygame


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.colors = ['black', 'red', 'blue']

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                coords = (
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                color = self.colors[self.board[row][col]]
                pygame.draw.rect(screen, color, coords)

        for row in range(self.height):
            for col in range(self.width):
                coords = (
                    self.left + col * self.cell_size,
                    self.top + row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(screen, 'white', coords, 1)

    def get_cell(self, mouse_pos):
        m_x, m_y = mouse_pos
        if m_x < self.left or m_x > self.left + self.width * self.cell_size or\
                m_y < self.top or m_y > self.top + self.height * self.cell_size:
            return None
        else:
            x = (m_y - self.top) // self.cell_size
            y = (m_x - self.left) // self.cell_size
            return x, y

    def on_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell is None:
            return
        x, y = cell
        self.board[x][y] = (self.board[x][y] + 1) % 3

    def get_click(self):
        ...


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    board = Board(5, 7)
    running = True
    screen.fill((0, 0, 0))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                board.on_click(mouse_pos)

        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
