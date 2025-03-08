import json
from sys import stdin

answers = stdin.readlines()

total = 0
with open('scoring.json') as file:
    data = json.loads(file.read())

    for index, answer in enumerate(answers):
        if answer == 'ok':
            for item in data['scoring']:
                if index + 1 in item['required_tests']:
                    total += item['points'] // len(item['required_tests'])
    print(total)
