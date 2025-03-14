import os

path = input("Input path:\n")


def human_read_format(size):
    count = 0
    list1 = ['Б', 'КБ', 'МБ', 'ГБ']

    while size > 1024:
        size /= 1024
        count += 1

    return f'{int(round(size, 0))}{list1[count]}'


total_files = []

for d_path, d_names, filenames in os.walk(path):

    for filename in filenames:
        filepath = os.path.join(d_path, filename)
        size = os.path.getsize(filepath)
        total_files.append((size, filepath))

    for dirname in d_names:
        dirpath = os.path.join(d_path, dirname)

        dir_size = 0
        for dirpath_root, _, dirfiles in os.walk(dirpath):
            for dirfile in dirfiles:
                dirfile_path = os.path.join(dirpath_root, dirfile)
                dir_size += os.path.getsize(dirfile_path)
        total_files.append((dir_size, dirpath))


largest_files = sorted(total_files, key=lambda x: x[0], reverse=True)[:10]

# для форматированного вывода
max_length = max([len(item[1]) for item in largest_files])

for item in largest_files:
    size, path = item
    _, name = path.rsplit(os.sep, maxsplit=1)
    h_size = human_read_format(size)

    print(f'{name:<{max_length}} - {h_size}')
