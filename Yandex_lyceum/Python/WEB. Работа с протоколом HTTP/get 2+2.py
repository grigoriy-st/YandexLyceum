import requests

address = input()
port = int(input())
a, b = int(input()), int(input())

# address = 'http://127.0.0.1'
# port = 7777
# a, b = 2, 4

url = f'http://{address}:{port}'
search_params = {
    "a": a,
    "b": b,
}
try:
    resp = requests.get(url, params=search_params)
    resp.raise_for_status()

    data = resp.json()
    result = data['result']
    check = data['check']

    sorted_result = sorted(result)

    print(' '.join(map(str, sorted_result)))
    print(check)
except requests.exceptions.RequestException as e:
    print('first:', e)
except Exception as e:
    print('second:', e)
