def print_long_words(text):
    string = list(text)
    vols = set('а, о, э, и, у, ы, е, ё, ю, я, a, e, i, o, u, y'.split(', '))
    err = '\\,.?><()\'\"@#$%^&[]'
    for i in range(len(string)):
        if string[i] in err:
            string[i] = (' ')
    string = ''.join(i for i in string).split()
    out = [i for i in string if len(set(i) & vols) > 3]
    [print(i) for i in out]
    #string = [i for text.split() for i in 
    pass
print_long_words('Как и в прочих заданиях этого урока, в вашем решении функция должна быть определена, но не должна вызываться.')
