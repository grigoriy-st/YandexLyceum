import os
import sys


def print_data(filename, count, num, sort):
    try:
        if os.path.isfile(os.getcwd() + filename):
            print('Файла нет')
            return

        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if sort:
            lines.sort()

        if num:
            [print(i, line.rstrip('\n')) for i, line in enumerate(lines)]
        else:
            [print(line.rstrip('\n')) for line in lines]

        if count:
            print(f'rows count: {len(lines)}')
    except Exception:
        print('ERROR')


def main():
    args = sys.argv[1:]

    if not args:
        print('Error')
        return

    count = '--count' in args
    num = '--num' in args
    sort = '--sort' in args
    
    for el in args:
        if '.' in el:
            filename = el

    if not filename:
        print('ERROR')
        return
    print_data(filename, count=count, num=num, sort=sort)


if __name__ == '__main__':
    main()
