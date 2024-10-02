def palindrome(s):
    if s[::-1] == s and s.isdigit():
        return True
    return False


def prime(num):
    result = [i for i in range(2, int(num) // 2 + 1) if int(num) % i == 0]
    if result:
        return False
    return True


def step(num):
    if not (num & (num - 1)) and num != 0:
        return True
    return False


def check_pin(string):
    string = string.split("-")
    a, b, c = string[0], string[1], int(string[2])
    a = prime(a)
    b = palindrome(b)
    c = step(c)
    if all([a, b, c]):
        return "Корректен"
    return "Некорректен"
print(check_pin('12- 1-1'))