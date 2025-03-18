import sys
import requests
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


def get_coords(place_name):
    """Получение координат по названию места."""
    apikey = '8013b162-6b42-4997-9691-77b7074026e0'
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={place_name}&format=json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        features = data.get('response', {}).get('GeoObjectCollection', {}).get('featureMember', [])

        if features:
            coords = features[0]['GeoObject']['Point']['pos']
            lon, lat = map(float, coords.split())
            return lat, lon


def get_map_with_markers(stadiums):
    """Получения карты с метками стадионов."""
    API_KEY = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'
    server_address = 'https://static-maps.yandex.ru/1.x/?'

    ll_spn = "ll=37.6156,55.7522&spn=0.1,0.1"
    markers = []

    for stadium, coords in stadiums.items():
        if coords:
            lat, lon = coords
            markers.append(f"{lon},{lat},pm2blm")

    markers_str = '~'.join(markers)
    map_request = f"{server_address}{ll_spn}&l=map&pt={markers_str}&apikey={API_KEY}"
    response = requests.get(map_request)

    return response.content


stadiums = {
    'Спартак': get_coords('стадион Спартак, Москва'),
    'Динамо': get_coords('стадион Динамо, Москва'),
    'Лужники': get_coords('стадион Лужники, Москва'),
}

map_image = get_map_with_markers(stadiums)

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
layout = QVBoxLayout()

label = QLabel()
pixmap = QPixmap()
pixmap.loadFromData(map_image)
label.setPixmap(pixmap)

layout.addWidget(label)
window.setLayout(layout)
window.show()

sys.exit(app.exec())
