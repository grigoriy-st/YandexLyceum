from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QVBoxLayout, QLabel, QPushButton

app = QApplication([])

# Создаем QTableWidget
tableWidget = QTableWidget(3, 3)  # 3 строки и 3 колонки

# Создаем QWidget для размещения в ячейке
widget = QWidget()
layout = QVBoxLayout()
label = QLabel("Это форма в ячейке")
button = QPushButton("Нажми меня")
layout.addWidget(label)
layout.addWidget(button)
widget.setLayout(layout)

# Устанавливаем QWidget в ячейку (0, 0)
tableWidget.setCellWidget(0, 0, widget)

# Отображаем таблицу
tableWidget.show()

app.exec_()