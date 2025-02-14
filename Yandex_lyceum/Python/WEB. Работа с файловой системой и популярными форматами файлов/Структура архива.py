import os
import zipfile


def print_zip_structure(filename):
    with zipfile.ZipFile(filename, 'r') as file:
        file_list = file.namelist()

        for el in file_list:
            level = el.count('/')

            _, file_name = el.rsplit(sep='/', maxsplit=1)
            print('  ' * level + file_name.rstrip('/'))


if __name__ == '__main__':
    print(os.chdir(r'C:\Users\grego\Documents\Projects\YandexLyceum\Yandex_lyceum\Python\WEB. Работа с файловой системой и популярными форматами файлов'))
    print_zip_structure('input.zip')
