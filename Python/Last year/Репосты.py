dict1 = {}
dict2 = {}
for i in range(int(input())):
    string = input().split()
    if i == 0:
        dict1[string[0]] = int(string[-1])
        dict2[string[0]] = []
        #print(list(dict1.keys())[0])
        continue
    name, post, num = string[0], string[4][:-1], int(string[-1])

    #print('/////////',f'name: {name}\tpost{post}\tnum{num}')
    if post in list(dict1.keys()):
        print('HELLLOOOO',dict2[dict2.keys()[0]])
        if post in list(dict2.keys())[0]:
            dict1[list(dict1.keys())[0]] += num
        dict1[post] += num
        
        dict2[list(dict2.keys())[0]] += name
        dict1[name] = num
    elif post not in list(dict1.keys()):
        print('------------',list(dict2.keys())[0])
        
        dict1[name] = num
    else:
        dict1[name] = num
print(dict1.items())
