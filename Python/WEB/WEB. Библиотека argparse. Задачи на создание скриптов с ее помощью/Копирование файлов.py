import argparse


def copy_file(src_file, dst_file, is_upper=False, lines=0):
    if not lines:
        lines = 0
    else:
        lines = int(lines)
    try:
        with open(src_file, 'r', encoding='utf-8') as source_f:
            with open(dst_file, 'w', encoding='utf-8') as destination_file:
                for i, line in enumerate(source_f):
                    if lines > 0 and i >= lines:
                        break
                    if is_upper:
                        line = line.upper()
                    destination_file.write(line)

    except Exception:
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--upper', action='store_true')
    parser.add_argument('--lines', type=str)
    parser.add_argument('source', type=str)
    parser.add_argument('destination', type=str)
    args = parser.parse_args()

    copy_file(args.source, args.destination, args.upper, args.lines)

