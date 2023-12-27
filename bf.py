string = [i for i in input()]
lenta = [0] * 30000
kout = 0
flag = False
fail_flag = False
for i in string:
    if flag:
        if i == '[':
            fail_flag = True
        if i != ']' and not fail_flag:
            if string[string.index(i) + 1] == '-':
                lenta[kout] = 0
            elif i == ".":
                print(lenta[kout % 30000])
            elif i == ">":
                kout += 1
            elif i == "<":
                kout -= 1
            continue
        else:
            flag = False
    if i == '[':
        if lenta[kout] == 0:
            flag = True
            continue
        else:
            if string[string.index(i) + 1] == '-':
                lenta[kout] = 0
            elif i == ".":
                print(lenta[kout % 30000])
            elif i == ">":
                kout += 1
            elif i == "<":
                kout -= 1
            flag = True
    if i == "+":
        lenta[kout % 30000] = (lenta[kout % 30000] + 1) % 256
    elif i == "-":
        lenta[kout % 30000] = (lenta[kout % 30000] - 1) % 256
    elif i == ".":
        print(lenta[kout % 30000])
    elif i == ">":
        kout += 1
    elif i == "<":
        kout -= 1
