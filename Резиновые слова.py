string = input()
if len(string) % 2 !=0:
    start = string[:len(string) // 2 + 1][::-1]
    end = string[len(string) // 2:]
    print(start,end)
    for i in range(len(string) // 2 + 1):
        if i == 0:
            print(' ' * (len(start) - 2),string[len(string) // 2], ' ' * (len(end) - 1))
            continue
        fir,sec = start[i], end[i]
        space = " " * (len(start) - (i + 1))
        print(f'{space}{fir}', end='')
        print(' ' * (i * 2 - 1), end='')
        print(f'{sec}{space}')

else:
    pass