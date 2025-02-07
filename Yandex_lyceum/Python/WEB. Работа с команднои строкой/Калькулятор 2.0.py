import sys

is_last_positive = True
result = 0
try:
    if len(sys.argv) >= 2:
        for arg in sys.argv[1:]:
            if '.' in arg or arg.isalpha():
                raise ValueError
            if arg.isdigit():
                result += int(arg) if is_last_positive else int(arg) * -1
                is_last_positive = False if is_last_positive else True
        print(result)

    elif len(sys.argv) == 1:
        print("NO PARAMS")
    else:
        print(0)
except Exception as e:
    print(type(e).__name__)
