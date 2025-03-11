import os
import zipfile


def human_read_format(size):
    count = 0
    list1 = ['Б', 'КБ', 'МБ', 'ГБ']

    while size > 1024:
        size /= 1024
        count += 1

    return f'{int(round(size, 0))}{list1[count]}'


def print_zip_structure(filename):
    with zipfile.ZipFile(filename, 'r') as zip_file:
        file_list = zip_file.namelist()

        for file_name in file_list:
            items = file_name.rstrip("/").split("/")
            spaces = (len(items) - 1)

            if file_name.endswith('/'):
                print("  " * spaces + items[-1])
            else:
                size = human_read_format(zip_file.getinfo(file_name).file_size)
                print("  " * spaces + items[-1] + f' {size}')


if __name__ == '__main__':
    print(os.chdir(r'C:\Users\grego\Documents\Projects\YandexLyceum\Yandex_lyceum\Python\WEB. Работа с файловой системой и популярными форматами файлов'))
    print_zip_structure('input.zip')
