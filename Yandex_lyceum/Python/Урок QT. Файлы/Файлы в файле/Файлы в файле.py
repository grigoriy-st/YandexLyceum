def transfer_measure_to_byte(size, measure):
    match measure:
        case 'B':
            return size
        case 'KB':
            return size * 1024
        case 'MB':
            return size * 1024 ** 2
        case 'GB':
            return size * 1024 ** 3
        case 'TB':
            return size * 1024 ** 4


def to_hight_measure(bytes):
    if bytes / (1024 ** 4) >= 1:
        return round(bytes / (1024 ** 4)), 'TB'
    elif bytes / (1024 ** 3) >= 1:
        return round(bytes / (1024 ** 3)), 'GB'
    elif bytes / (1024 ** 2) >= 1:
        return round(bytes / (1024 ** 2)), 'MB'
    elif bytes / 1024 >= 1:
        return round(bytes / 1024), 'KB'
    else:
        return bytes, 'B'


with open("input.txt", 'r', encoding='utf-8') as f:
    try:
        strings = f.readlines()
        if strings:
            dict_ext = {}

            for line in strings:
                file_name, size, measure = line.rstrip().rsplit(maxsplit=2)
                file_name, ext = file_name.split('.')
                measure_in_bytes = transfer_measure_to_byte(int(size), measure)

                if ext not in dict_ext:
                    dict_ext[ext] = [int(measure_in_bytes), [file_name]]
                else:
                    dict_ext[ext][0] += int(measure_in_bytes)
                    dict_ext[ext][1].append(file_name)

            # write in file
            with open("output.txt", 'w', encoding='utf-8') as out:
                for ext in sorted(dict_ext.keys()):
                    name_list = sorted(dict_ext[ext][1])
                    [out.write(f'{name}.{ext}\n') for name in name_list]
                    out.write('----------\n')

                    size, measure = to_hight_measure(dict_ext[ext][0])
                    out.write(f'Summary: {size} {measure}\n\n')

        else:
            ...

    except FileNotFoundError:
        ...
