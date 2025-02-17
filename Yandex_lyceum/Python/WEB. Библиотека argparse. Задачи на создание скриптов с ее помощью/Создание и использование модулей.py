import argparse

def count_lines(path_to_file):
    line_count = 0
    try:
        with open(path_to_file, 'r', encoding='utf-8') as file:
            for line in file:
                line_count += 1
    except Exception:
        line_count = 0
    return line_count


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', type=str)
    args = parser.parse_args()

    print(count_lines(args.file))

