""" Скрипт неправильно наносит метки на карту. В основном код """
import os
import sys
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

API_KEY = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'

os.chdir('WEB. Знакомство с API')


def get_map(coords: tuple):
    x, y = coords.split(',')
    url = f'https://static-maps.yandex.ru/1.x/?ll={x},{y}&spn=0.05,0.05&l=map&apikey={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.content
    else:
        print("Ошибка при получении карты:", response.status_code)
        return None


class MapWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 600, 450)

        # Данные для запросов
        self.server_address = 'https://static-maps.yandex.ru/v1?'
        self.moscow_coords = self.get_coords('Москва').replace(' ', ',')
        self.ll_spn = f'll={self.moscow_coords}&spn=0.05,0.05'

        self.stadiums = {
            'Спартак': None,
            'Динамо': None,
            'Лужники': None,
        }

        for stadium in self.stadiums.keys():
            self.stadiums[stadium] = self.get_coords(f'стадион {stadium}, город Москва')

        layout = QVBoxLayout()

        # Получаем карту с использованием координат Москвы
        map_image_data = get_map(self.moscow_coords)
        if map_image_data:
            with open("map_image.png", "wb") as f:
                f.write(map_image_data)

            self.map_pixmap = QPixmap("map_image.png")
            self.map_label = QLabel()
            self.map_label.setPixmap(self.map_pixmap)

            # Загружаем метку и изменяем ее размер
            self.marker_pixmap = QPixmap("Map Marker.png").scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)  

            # Устанавливаем метку в центр карты
            layout.addWidget(self.map_label)

            # Отображаем метки для каждого стадиона
            for stadium, coords in self.stadiums.items():
                if coords:
                    self.add_marker(layout, coords, stadium)

            self.setLayout(layout)

    def add_marker(self, layout, coords, stadium_name):
        ''' Добавление маркера на карту. '''
        x, y = map(float, coords.split(','))

        # Преобразуем координаты в пиксели
        map_width, map_height = self.map_pixmap.width(), self.map_pixmap.height()
        center_x, center_y = map(float, self.moscow_coords.split(','))

        # Преобразование координат в пиксели (это упрощенная версия)
        pixel_x = int((x - center_x) * (map_width / 0.05) + (map_width / 2))
        pixel_y = int((y - center_y) * (map_height / 0.05) + (map_height / 2))
        print(pixel_x, pixel_y)
        # Создаем QLabel для метки
        marker_label = QLabel()
        marker_label.setPixmap(self.marker_pixmap)

        # Устанавливаем метку в нужные координаты
        # marker_label.setGeometry(pixel_x - self.marker_pixmap.width() // 2, 
        #                         pixel_y - self.marker_pixmap.height(), 
        #                         self.marker_pixmap.width(), 
        #                         self.marker_pixmap.height())
        marker_label.setGeometry(20, 20, 30, 30)
        layout.addWidget(marker_label)

    def get_coords(self, place_name):
        ''' Получение координат по месту. '''
        API_KEY = '8013b162-6b42-4997-9691-77b7074026e0'
        url = (
            "https://geocode-maps.yandex.ru/1.x/"
            "?apikey={apikey}"
            "&geocode={address}"
            "&format=json"
        ).format(
            apikey=API_KEY,
            address=place_name
        )

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if 'response' in data and 'GeoObjectCollection' in data['response']:
                features = data['response']['GeoObjectCollection']['featureMember']
                if features:
                    coords = features[0]['GeoObject']['Point']['pos']
                    # Replace space with a comma
                    return coords.replace(' ', ',')
        return None


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())