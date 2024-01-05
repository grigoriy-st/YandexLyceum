list1 = []
output = []
for i in range(int(input())):
    temp = [input() for i in range(int(input()))]
    list1 += temp
for i in set(list1):
    if list1.count(i) >1:
        output.append(list1.count(i))
print(len(output), sum(output))
