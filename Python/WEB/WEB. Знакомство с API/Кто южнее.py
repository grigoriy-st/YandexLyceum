import requests


def get_coords(city):
    apikey = '8013b162-6b42-4997-9691-77b7074026e0'
    url = f"https://geocode-maps.yandex.ru/1.x/?apikey={apikey}&geocode={city}&format=json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        features = data.get('response', {}).get('GeoObjectCollection', {}).get('featureMember', [])
        if features:
            coords = features[0]['GeoObject']['Point']['pos']
            lon, lat = map(float, coords.split())
            return lat
    return None


def get_southernmost_city(cities):
    city_coords = {city: get_coords(city) for city in cities}

    data = {}
    for city, lat in city_coords.items():
        if lat is not None:
            data[city] = lat
            print(city, ":", lat)

    if not data:
        return "Не удалось определить координаты городов."
    return min(city_coords, key=city_coords.get)


cities = input("Введите список городов через запятую: ").split(',')
cities = [city.strip() for city in cities if city.strip()]
if cities:
    southernmost_city = get_southernmost_city(cities)
    print(f"Самый южный город: {southernmost_city}")
else:
    print("Список городов пуст.")

# Владивосток, Санкт-Петербург, Москва, Сочи, Казань
# Омск, Тара
