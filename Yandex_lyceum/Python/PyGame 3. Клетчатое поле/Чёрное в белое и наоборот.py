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
        self.colors = ['black', 'white']

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
        if m_x > self.width * self.cell_size or\
                m_y > self.height * self.cell_size:
            print(None)
        x = m_x // self.cell_size
        y = m_y // self.cell_size
        print(x, y)

    def on_click(self, screen, mouse_pos):
        m_x, m_y = mouse_pos
        x = m_x // self.cell_size
        y = m_y // self.cell_size

        for cell in range(self.height):
            coords = (
                    self.left + x * self.cell_size,
                    self.top + cell * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
            print("Это x и cell", x, cell)
            if x < self.height and cell < self.width:
                color = self.colors[self.board[x][cell]]
                pygame.draw.rect(screen, color, coords)
                self.board[x][cell] = (self.board[x][cell] + 1) % 2

        for cell in range(self.width):
            if cell != x:
                coords = (
                    self.left + cell * self.cell_size,
                    self.top + y * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
            color = self.colors[self.board[cell][y]]
            pygame.draw.rect(screen, color, coords)
            self.board[cell][y] = (self.board[cell][y] + 1) % 2

    def get_click(self):
        ...


def main():
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
                board.get_cell(mouse_pos)
                board.on_click(screen, mouse_pos)

        board.render(screen)
        pygame.display.flip()


if __name__ == '__main__':
    main()
