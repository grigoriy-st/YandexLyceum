import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QTabWidget Example')
        self.setGeometry(100, 100, 400, 300)

        self.tabs = QTabWidget(self)
        self.setCentralWidget(self.tabs)

        # Создаем вкладки
        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.tabs.addTab(self.tab1, 'Tab 1')
        self.tabs.addTab(self.tab2, 'Tab 2')

        self.tab1_layout = QVBoxLayout()
        self.tab1_layout.addWidget(QLabel('This is Tab 1'))
        self.tab1.setLayout(self.tab1_layout)

        self.tab2_layout = QVBoxLayout()
        self.tab2_layout.addWidget(QLabel('This is Tab 2'))
        self.tab2.setLayout(self.tab2_layout)

        # Подключаем сигнал изменения вкладки
        self.tabs.currentChanged.connect(self.on_tab_changed)

        # Дополнительный интерфейс (например, кнопка)
        self.extra_interface = QPushButton('Extra Interface', self)
        self.extra_interface.setGeometry(10, 220, 150, 30)
        self.extra_interface.hide()  # Скрываем его по умолчанию

    def on_tab_changed(self, index):
        if index == 1:  # Если переключились на Tab 2
            self.extra_interface.show()  # Показываем дополнительный интерфейс
        else:
            self.extra_interface.hide()  # Скрываем дополнительный интерфейс

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())