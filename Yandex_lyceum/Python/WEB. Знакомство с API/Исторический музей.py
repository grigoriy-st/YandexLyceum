import requests

apikey = '8013b162-6b42-4997-9691-77b7074026e0'

city_data = {
    'Хабаровск': None,
    'Уфа': None,
    'Нижний Новгород': None,
    'Калининград': None,
}

for city in city_data.keys():
    url = (
            "https://geocode-maps.yandex.ru/1.x/"
            "?apikey={apikey}"
            "&geocode={address}"
            "&format=json"
        ).format(
            apikey=apikey,
            address=city,
              )

    response = requests.get(url)
    city_data[city] = response

for city in city_data.keys():
    if city_data[city].status_code == 200:
        data = city_data[city].json()

        if 'response' in data and 'GeoObjectCollection' in data['response']:
            features = data['response']['GeoObjectCollection']['featureMember']
            if features:
                area = features[0]['GeoObject']['metaDataProperty']
                area = area['GeocoderMetaData']

                city_area = area['AddressDetails']['Country']
                city_area = city_area['AdministrativeArea']
                city_area = city_area['AdministrativeAreaName']

                print(f'{city}: {city_area}')
            else:
                print('Адрес не найден')
    else:
        print('Ошибка выполнения запроса')
