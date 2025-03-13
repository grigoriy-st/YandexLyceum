import csv

with open('alpha_oriona.csv', 'r', encoding='utf-8') as file:
    data = list(csv.DictReader(file, delimiter=';'))

max_length = 0
max_start_date_time = ""
current_length = 1

last_luminosity = int(data[0]['luminosity'])
start_date_time = f"{data[0]['date']} {data[0]['time']}"

for i in range(1, len(data)):
    cur_luminosity = int(data[i]['luminosity'])

    if cur_luminosity <= last_luminosity:
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            max_start_date_time = start_date_time

        current_length = 1
        start_date_time = f"{data[i]['date']} {data[i]['time']}"

    last_luminosity = cur_luminosity

if current_length > max_length:
    max_length = current_length
    max_start_date_time = start_date_time

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(f"{max_length}\n")
    file.write(max_start_date_time)