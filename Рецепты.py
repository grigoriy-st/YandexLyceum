num = int(input())
output = []
food = set([input() for i in range(num)])
for i in range(int(input())):
    ingradients = set()
    word = input()
    ingrs = int(input())
    ingradients = set([input() for j in range(ingrs)])
    if len(ingradients & food) == len(ingradients):
        output.append(word)
[print(i) for i in output]
