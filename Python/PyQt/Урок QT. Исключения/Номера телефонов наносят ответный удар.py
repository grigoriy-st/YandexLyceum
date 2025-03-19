try:
    num = ''.join(input().split())

    error = False
    if not (num.startswith("+7") or num.startswith("8")) \
       or num[0] == '-' or num[-1] == '-':
        raise TypeError("неверный формат")

    num = num.replace('+7' if num.startswith("+7") else "8", "", 1)

    for i in range(len(num) - 1):
        if num[i] == '-' and num[i + 1] == '-':
            raise TypeError("неверный формат")

    if (num.count('(') != num.count(')')) or num.count('(') > 1:
        raise TypeError("неверный формат")

    if '(' in num and ')' in num:
        if num.index('(') > num.index(')'):
            raise TypeError("неверный формат")

    num = num.replace('(', '')
    num = num.replace(')', '')
    num = num.replace('-', '')

    operator_nums = {
        'МТС': [list(range(910, 920)), list(range(980, 990))],
        'МегаФон': [list(range(920, 940))],
        'Билайн': [list(range(902, 906)), list(range(960, 970))],
    }

    if not num.isdigit():
        raise TypeError("неверный формат")

    if len(num) != 10:
        raise ValueError("неверное количество цифр")

    first_three_figure = int(num[:3])
    num_have_operator = False

    for operator in operator_nums.keys():
        for scope in operator_nums[operator]:
            if first_three_figure in scope:
                num_have_operator = True

    if not num_have_operator:
        raise ValueError("не определяется оператор сотовой связи")

except ValueError as ve:
    print(ve)
except TypeError as te:
    print(te)
else:
    print('+7' + num)
