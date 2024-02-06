def placeholder(*lines, **holders) -> dict:
    dict1 = {}
    sign = '!@#$%^&*()_+-\\,<>/|.?'
    # сначала пробегай по шаблонам, а потом по строкам
    # сейчас ты делаешь наооборот
    for i in range(len(lines)):
        temp = []
        # print(lines[i].split())
        for l in lines[i].split():
            if set(sign) & set(l):
                res = list(set(sign) & set(l))
                temp[-1] = temp[-1] + str(res[0])
            else:
                temp.append('_')
        temp = ' '.join(i for i in temp)
        for j in holders:
            # print(f'{holders[j][1:]} == {temp}')
            if holders[j][1:] == temp:
                if holders[j] in dict1:
                    dict1[holders[j]] += temp
                else:
                    dict1[holders[j]] = [temp]
    return dict1


lines = ["Look at the boy, he has a toy.",
         "Look at me.", "I am happy.",
         "Here is the kitchen where Mother cooks for me.",
         "What are little boys made of?",
         "What are little girls made of?",
         "Look at the girl, she has a doll."]
holders = {"h1": "|_ _ _ _, _ _ _ _.",
           "h2": "|_ _ _.", "h3": "|_ _ _ _ _ _?"}
print(placeholder(*lines, **holders))
for k, v in placeholder(*lines, **holders).items():
    print(k, "->", *v)