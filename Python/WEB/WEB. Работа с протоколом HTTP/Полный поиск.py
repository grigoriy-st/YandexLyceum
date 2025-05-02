import sys
from io import BytesIO
import requests
from PIL import Image

def get_map_scale_params(toponym):
    try:
        envelope = toponym["boundedBy"]["Envelope"]
        left, bottom = envelope["lowerCorner"].split(" ")
        right, top = envelope["upperCorner"].split(" ")
        
        width = abs(float(right) - float(left))
        height = abs(float(top) - float(bottom))
        
        # Добавляем небольшой зазор вокруг объекта
        width = max(width, 0.005)
        height = max(height, 0.005)
        
        return f"{width},{height}"
    except KeyError:
        # Если нет данных о границах, возвращаем значение по умолчанию
        return "0.005,0.005"

def main():
    if len(sys.argv) < 2:
        print("Использование: python search.py <адрес>")
        return

    toponym_to_find = " ".join(sys.argv[1:])
    print(f"Поиск адреса: {toponym_to_find}")

    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",  # Замените на ваш действительный ключ
        "geocode": toponym_to_find,
        "format": "json"
    }

    try:
        response = requests.get(geocoder_api_server, params=geocoder_params)
        response.raise_for_status()  # Проверяем HTTP ошибки
        
        json_response = response.json()
        
        # Проверяем, есть ли результаты
        feature_members = json_response["response"]["GeoObjectCollection"]["featureMember"]
        if not feature_members:
            print("Адрес не найден")
            return
            
        toponym = feature_members[0]["GeoObject"]
        toponym_coordinates = toponym["Point"]["pos"]
        toponym_longitude, toponym_lattitude = toponym_coordinates.split(" ")
        print(f"Найденные координаты: {toponym_longitude}, {toponym_lattitude}")

        spn = get_map_scale_params(toponym)
        print(f"Параметры масштаба: {spn}")

        map_api_server = "https://static-maps.yandex.ru/1.x"
        map_params = {
            "ll": ",".join([toponym_longitude, toponym_lattitude]),
            "spn": spn,
            "l": "map",
            "pt": f"{toponym_longitude},{toponym_lattitude},pm2dgl",
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b"  # Замените на ваш действительный ключ
        }

        response = requests.get(map_api_server, params=map_params)
        response.raise_for_status()

        im = BytesIO(response.content)
        opened_image = Image.open(im)
        opened_image.show()

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except KeyError as e:
        print(f"Ошибка при обработке ответа: отсутствует ключ {e}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()