import requests


GEOCODER_API_KEY = '8013b162-6b42-4997-9691-77b7074026e0'  
STATIC_MAP_API_KEY = 'f3a0fe3a-b07e-4840-a1da-06f18b2ddf13'  

WIDTH, HEIGHT = 600, 450

place_name = input("Введите страну, город или адрес: ").strip()

if not place_name:
    print("Вы ничего не ввели.")
    exit()

geocoder_url = (
    f'https://geocode-maps.yandex.ru/1.x/'
    f'?apikey={GEOCODER_API_KEY}&geocode={place_name}&format=json'
)

geo_response = requests.get(geocoder_url)

if geo_response.status_code != 200:
    print("Ошибка геокодирования:", geo_response.status_code)
    exit()

try:
    geo_json = geo_response.json()
    geo_object = geo_json["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
    pos = geo_object["Point"]["pos"]
    name = geo_object["name"]
    longitude, latitude = pos.split()
except (IndexError, KeyError, ValueError):
    print("Не удалось найти координаты по введённому адресу.")
    exit()


map_url = (
    f'https://static-maps.yandex.ru/1.x/'
    f'?ll={longitude},{latitude}'
    f'&z=6&l=map&size={WIDTH},{HEIGHT}'
    f'&pt={longitude},{latitude},pm2rdm'
    f'&apikey={STATIC_MAP_API_KEY}'
)

map_response = requests.get(map_url)

if map_response.status_code == 200:
    file_name = "map_image.png"
    with open(file_name, "wb") as f:
        f.write(map_response.content)
    print(f"✅ Карта '{name}' сохранена как {file_name}")
else:
    print("Ошибка при загрузке карты:", map_response.status_code)
