num = 10 + 1
list1 = list(range(2, num))
temp_output = None

def prime(num):
    '''Проверка числа на простоту'''
    result = [i for i in range(2, int(num) + 2) if int(num) % i == 0]
    if result:
        return False
    return True


while temp_output != list1:
    temp_output = list1
    for i in list1:
        simple_num = list1[0]
        if i % simple_num == 0 and prime(simple_num):
            list1.remove(i)
    find_1 = [i for i in range(len(list1)) if list1[i] < list1[0]][0]
    print(find_1)
    list1[list1.index(find_1)] = list1[0]
print(list1)
