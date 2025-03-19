from PyQt6.QtWidgets import QApplication

from main import MainWindow

class Controller:
    def __init__(self, main_window):
        self.main_window = main_window

    def update_button_text(self, new_text):
        self.main_window.change_button_text(new_text)

if __name__ == "__main__":
    app = QApplication([])
    main_window = MainWindow()
    controller = Controller(main_window)

    # Изменяем текст кнопки через контроллер
    controller.update_button_text("New Button Text")

    main_window.show()
    app.exec()