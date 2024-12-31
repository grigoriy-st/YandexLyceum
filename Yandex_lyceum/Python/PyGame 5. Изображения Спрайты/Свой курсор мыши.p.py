import sys
import pygame
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Инициализация Pygame
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Custom Cursor with Pygame")

        # Загрузка изображения курсора
        self.cursor_image = pygame.image.load("arrow.png").convert_alpha()
        self.cursor_rect = self.cursor_image.get_rect(center=(0, 0))

        # Установка фона
        self.background_color = (0, 0, 0)  # Черный цвет

        # Таймер для обновления
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_pygame)
        self.timer.start(16)  # Обновление примерно 60 FPS

        self.setWindowTitle("Pygame Cursor Example")
        self.setGeometry(100, 100, 800, 600)

    def update_pygame(self):
        # Проверка, находится ли курсор в фокусе
        if pygame.mouse.get_focused():
            self.screen.fill(self.background_color)

            # Получение позиции курсора
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.cursor_rect.center = (mouse_x, mouse_y)

            # Отрисовка курсора
            self.screen.blit(self.cursor_image, self.cursor_rect)

            # Обновление экрана
            pygame.display.flip()

    def closeEvent(self, event):
        pygame.quit()
        event.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())