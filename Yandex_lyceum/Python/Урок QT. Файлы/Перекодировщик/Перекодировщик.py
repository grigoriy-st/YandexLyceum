f = open("cyrillic.txt", mode="r", encoding="utf-8")

strings = f.readlines()

table = {
    "й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",  
    "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",  
    "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",  
    "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",  
    "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'",  
    "б": "b", "ю": "ju", "ё": "jo"
}

out = open("transliteration.txt", mode="w", encoding="utf-8")
table_keys = table.keys()

for line in strings:
    for let in line:
        if let.lower() in table_keys:
            if let.islower():
                new_let = table[let.lower()].lower()
            else:
                new_let = table[let.lower()].title()
            out.write(new_let)
        else:
            out.write(let)

f.close()
out.close()
