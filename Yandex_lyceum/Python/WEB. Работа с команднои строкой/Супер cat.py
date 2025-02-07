import sys

args = sys.argv
last_cmd = None

for arg in args[1:]:
    if arg in ['--num', '--count', '--sort']:
        last_cmd = arg
        continue

    if last_cmd == '--num':
        row_num = 0

        with open(arg, "r", encoding='utf-8') as file:
            while True:
                line = file.readline().rstrip("\n")
                if not line:
                    break

                print(f'{row_num} {line}')
                row_num += 1

