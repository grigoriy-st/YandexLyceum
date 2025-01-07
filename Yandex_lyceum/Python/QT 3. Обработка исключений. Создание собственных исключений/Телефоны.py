country_codes = ['+7', '8', '+359', '+55', '+1']


def right_num_start(num):
    for code in country_codes:
        if num.startswith(code):
            return True

    return False


def num_have_country_code(num):
    for code in country_codes:
        if num.startswith(code):
            return True, code

    return False, None


try:
    num = ''.join(input().split())

    if num[0] == '-' or num[-1] == '-' and right_num_start(num):
        raise TypeError("неверный формат")

    for i in range(len(num) - 1):
        if num[i] == '-' and num[i + 1] == '-':
            raise TypeError("неверный формат")

    if (num.count('(') != num.count(')')) or num.count('(') > 1:
        raise TypeError("неверный формат")

    if '(' in num and ')' in num:
        if num.index('(') > num.index(')'):
            raise TypeError("неверный формат")

    have_country_code, code = num_have_country_code(num)
    if not have_country_code:
        raise ValueError('не определяется код страны')
    else:

        if len(num.lstrip('+')) != 11:
            raise ValueError("неверное количество цифр")

        num = num.replace(code, '', 1)



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


    first_three_figure = int(num[:3])
    print(first_three_figure)
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
