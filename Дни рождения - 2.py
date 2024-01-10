dict1 = {}
for i in range(int(input())):
    string = input().split()
    name, m, d = string[0], string[-1], string[1]
    if m not in dict1:
        dict1[m] = [(int(d), name)]
    else:
        dict1[m].append((int(d), name))
list1 = [input() for i in range(int(input()))]
for i in list1:
    if i in dict1:
        temp = []
        if len(dict1[i]) != 1:
            for j in sorted(dict1[i], key=len):
                temp.append((j[0], j[1]))
            output = [str(i) for j in sorted(temp, reverse=True) for i in j]
            print(' '.join(i for i in output[::-1]))
        else:
            for j in sorted(dict1[i], key=len):
                temp.append(j[0])
                temp.append(j[1])
            print(' '.join(str(i) for i in temp[::-1]))
    else:
        print()
