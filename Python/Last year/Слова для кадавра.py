import re
string = input()
list1 = []
word = input()
while word:
    list1.append(word)
    word = input()
rstring = '^'
for i in string:
    if i == '1':
        rstring += '[^ауоыиэяюёе]'
    elif i == '0':
        rstring += '[ауоыиэяюёе]'
    elif i == '?':
        rstring += '[а-я]'
    elif i == '*':
        rstring += '.*'
rstring += '$'
output = []
for j in list1:
    if re.search(rstring, j):
        output.append(j)
if output:
    [print(i) for i in output]
else:
    print('Есть нечего, значить!')