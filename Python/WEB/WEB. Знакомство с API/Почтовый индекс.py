import requests

address = "Москва, Петровка, 38"
apikey = '8013b162-6b42-4997-9691-77b7074026e0'

url = (
        "https://geocode-maps.yandex.ru/1.x/"
        "?apikey={apikey}"
        "&geocode={address}"
        "&format=json"
      ).format(
        apikey=apikey,
        address=address
              )
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    if 'response' in data and 'GeoObjectCollection' in data['response']:
        features = data['response']['GeoObjectCollection']['featureMember']
        if features:
            mail_code = features[0]['GeoObject']['metaDataProperty']
            mail_code = mail_code['GeocoderMetaData']['Address']['postal_code']

            print('Почтовый индекс:', mail_code)
        else:
            print('Адрес не найден')
else:
    print('Ошибка выполнения запроса')
