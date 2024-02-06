def eratosthenes(num):
    list1 = range(2, num + 1)
    output = []
    while True:
        filter_l = list(filter(lambda x: x % 2, list1))
        if filter_l != list1:
            list1 = filter_l
            for i in range(1, len(list1)):
                if list1[i] % list1[0] == 0:
                    del list1[i]
                if list1[i] > i:
                    list1[i] = i
                output.append()
        break
    print(list1)


eratosthenes(15)