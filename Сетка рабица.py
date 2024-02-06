num = int(input())
def net(num):
    string1 = r'/ \_/'
    string2 = r'\_/ \\'
    for i in range(num):
        temp = ''
        for j in range(1, num):
            print(string1[j % num], end='')
            temp += string1[j]

        print()
            # else:
            #     print(string2[num:])
net(num)