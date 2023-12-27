dict1 = {}
for i in range(int(input())):
    string = input().split()
    name, m, d = string[0], string[-1], string[1]
    if m not in dict1:
        dict1[m] = [(d, name)]
    else:
        dict1[m].append((d, name))
list1 = [input() for i in range(int(input()))]
for i in list1:
    
    if i in dict1:
        print(dict1[i])
        temp = []
        for j in sorted(dict1[i], key=lambda dict1: dict1[i][0]):
            temp.append(j[0])
            temp.append(j[1])
        print(' '.join(str(i) for i in temp))
    else:
        print()
