import json
import zipfile

def count_people_in_moscow(zip_filename):
    people_count = 0

    with zipfile.ZipFile(zip_filename, 'r') as zip_file:
        file_list = zip_file.namelist()

        for file_name in file_list:
            if file_name.endswith('.json'):
                with zip_file.open(file_name) as file:
                    try:
                        data = json.load(file)

                        if isinstance(data, dict) and data.get('city') == 'Москва':
                            people_count += 1
                    except json.JSONDecodeError:
                        print(f"Ошибка декодирования JSON в файле: {file_name}")

    print(people_count)

zip_filename = 'input.zip'
count_people_in_moscow(zip_filename)

