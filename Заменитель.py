def placeholder(*lines, **holders):
    sign = '!@#$%^&*()_+-\\,<>/|.?'
    dict1 = {}
    for i in holders:    # заполнение нового словаря
        dict1[holders[i]] = []
    for st in dict1:
        for i in range(len(lines)):
            temp = []    # строка в шаблонном виде для дальнейшео сравнения
            for line in lines[i].split():
                if set(sign) & set(line):
                    find_sign = list(set(sign) & set(line))
                    if line.split(find_sign[0]):    # если в строке помимо символа из sing есть ещё и слово 
                        temp.append('_')
                    temp[-1] = temp[-1] + str(find_sign[0])
                else:
                    temp.append('_')
            temp = ' '.join(i for i in temp)    # связка всех элементов (последний этап создания шаблона на основе строки в lines)
            if temp == st.replace('|_', '_') and temp not in dict1[st]:    # за
                dict1[st].append(lines[i])
                dict1[st] = sorted(dict1[st]) # сортировка в алфавитном порядке
    for i in list(dict1):
        if not dict1[i]:
            del dict1[i]
    return dict1

lines = ["Look at me.", "Its color is pink", 
         "What are little girls made of?", 
         "Its very big!", "I am happy.", 
         "He ate a butcher and a half,", 
         "It likes to play.", "This is a pig!", 
         "Look at the girl, she has a doll.", 
         "It is warm and fat."]
holders = {'h1': '|_ _ _.', 'h2': '|_ _ _ _, _ _ _ _.', 
           'h3': '|_ _ _ _.', 'h4': '|_ _ _ _ _ |_ _ _ _.', 
           'h5': '|_ _ _ _ _ _?', 'h6': '|_, _, _ _, _ |_ _ _ _ _.', 
           'h7': '|_ _, |_ _!', 'h8': '|_ _ _!', 'h9': '|_ _ _ _, _ _ _ _,'}
for k, v in placeholder(*lines, **holders).items():
    print(k, "->", *v)
'''Заменять можно много чего. Например, в схеме предложения нижнее подчеркивание заменяет слово. 
А черточка с вертикальной чертой спереди заменяет слово, начинающееся с большой буквы.

Напишите функцию placeholder(), которая множество строк сортирует по заменителям.
Функция принимает произвольное количество позиционных аргументов-строк и произвольное 
количество именованных аргументов, значениями которых являются схемы различных предложений. 
Слова заменены нижним подчеркиванием или вертикальной чертой с нижним подчеркиванием, знаки препинания 
стоят на своих местах.
Функция возвращает словарь, ключи которого – схемы предложений, значения – списки предложений с такой схемой, 
отсортированные по алфавиту. Если для предложения нет подходящей схемы, оно никуда не записывается, 
если для схемы не нашлось предложений, такой ключ не создается.'''
