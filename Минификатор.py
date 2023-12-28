num = int(input())
list1 = []
flag = True
ou_string = ''
close_instr = False
for i in range(num):
    string = input()
    if string[:4] != '    ':
        string = ' '.join(string.split())
    for j in range(len(string)):
        if 'print' in string:
            if string[j] == '(' and string[j + 1] == '\'':
                flag = False
            elif string[j] == ')' and string[j - 1] in '\' ':
                flag = True
            elif '(\'' not in string and string[:4] == '    ':
                ou_string = '    ' + ' '.join(string.split())
                ou_string = ou_string[:ou_string.rindex('#')]
        if string[j] == '#' and flag:
            ou_string = string[:j]
    if ou_string:
        outs = ou_string
    else:
        outs = string
    if len(outs[outs.rfind('\''):-1]) >= 2:
        outs = outs[:outs.rfind('\'') + 1] + ' )'
    list1.append(outs)
    ou_string = ''
[print(i) for i in list1]
