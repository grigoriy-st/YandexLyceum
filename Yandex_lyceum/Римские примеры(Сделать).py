def transform(num):
    num = str(num)
    list1 = []
    while len(num) > 1:
        for i in reversed(string):
            if len(str(int(num) % i).lstrip('0')) == 1:
                # print(string[i] , (int(num) % i))
                if num in string:
                    list1.append(string[num])
                list1.append(string[i] * (int(num) % i))

                start = len(num) - len(str(i)) + 1
                num = num[start:]
    return list1
ones = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
string = {
    1: 'I',
    5: 'V',
    10: 'X',
    50: 'L',
    100: 'C',
    500: 'D',
    1000: 'M'
}

print(transform(501))
