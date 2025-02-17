import os
import sys

from pprint import pprint
import pygame
import requests


def get_coords(place_name):
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
                return coords
            else:
                print('Ошибка при получении координат')
    else:
        print('Статус != 200')


API_KEY = '8013b162-6b42-4997-9691-77b7074026e0'
server_address = 'https://static-maps.yandex.ru/v1?'
moscow_coords = get_coords('Москва').replace(' ', ',')
ll_spn = f'll={moscow_coords}&spn=0.002,0.002'

stadiums = {
    'Спартак': None,
    'Динамо': None,
    'Лужники': None,
}

for stadium in stadiums.keys():
    stadiums[stadium] = get_coords(f'стадион {stadium}, город Москва')
    print(f'{stadium}: {stadiums[stadium]}')

pprint(stadiums)

print(server_address)
print(ll_spn)
map_request = f"{server_address}{ll_spn}&apikey={API_KEY}"
response = requests.get(map_request)

if not response:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

# Запишем полученное изображение в файл.
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
screen.blit(pygame.image.load(map_file), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой фа
