with open('pipes.txt', encoding='utf-8') as file:
    data = file.readlines()

pipes = [1 / float(line)
         if line and float(line) != 0.0 else 0
         for line in data[:-2]]

result = 0
for num in list(map(int, data[-1].split())):
    result += pipes[num - 1]

with open('time.txt', 'w', encoding='utf-8') as out:
    out.write(str(60 * (1 / result)))
