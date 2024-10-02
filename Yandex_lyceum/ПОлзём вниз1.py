string = list(input())
list1 = []
symb = string.pop(0)
temp = []
for i in range(len(string)):
    if i == len(string) - 1:
        z= ''.join(i for i in temp)
        list1.append(z)
    if temp == []:
        temp.append(string[i])
    elif string[i] == temp[-1]:
        temp.append(string[i])
    elif string[i] != temp[-1]:
        z= ''.join(i for i in temp)
        list1.append(z)
        temp = [string[i]]
print(list1)
pos = 0


for i in range(len(list1)):
    if 'V' in list1[i]:
        lens = len(list1[i])
        for j in range(lens):
            if j == lens - 1:
#Редачь этот код
                if '<' in list1[i + 1]:
                    pos -= lens - 1
                    
                    list1[i + 1] = list1[i + 1] +'<' * lens
                    continue
                ''' if '>' in list1[i + 1]:
                    pos -= lens - 1
                    list1[i + 1] = list1[i + 1] +'<' * lens
                    continue'''
            
#-------------
            print(' ' * pos, symb,sep='')
    elif '>' in list1[i]:
        print(symb * len(list1[i]))
        pos += len(list1[i])
    elif '<' in list1[i]:
        
        pos -= len(list1[i])
        print(' ' * pos,symb * len(list1[i]), sep='')
        