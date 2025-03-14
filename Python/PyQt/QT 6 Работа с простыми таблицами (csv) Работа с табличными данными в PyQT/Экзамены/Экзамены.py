from sys import stdin

n, m = list(map(int, input().split()))
raw_data = stdin.readlines()

with open('exam.csv', 'w', encoding='utf-8') as file:
    file.write('Фамилия;имя;результат 1;результат 2;результат 3;сумма\n')
    for line in raw_data:
        famile, name, e1, e2, e3 = line.split()
        summary = int(e1) + int(e2) + int(e3)

        exp1 = int(e1) >= m and int(e2) >= m and int(e3) >= m
        exp2 = summary >= n
        print(exp1, exp2)
        if exp1 and exp2:
            file.write(';'.join([famile, name, e1, e2, e3, str(summary)]) + '\n')
