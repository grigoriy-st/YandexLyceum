'''
Программа работает только с латинским алфавитом
Тестировал код Морзе на сайте https://morsedecoder.com/ru/
На этом сайте строка ' / ' означает пробел и перенос строки, поэтому
я добавил её при кодировании сообщения.

В правое окно на сайте можно вписать код Морзе
и в левом окне будет отображён расшифрованный текст
'''
MorseCode = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def get_key(value) -> str:
    '''Функция поиска буквы в словаре(по значению)'''
    global MorseCode
    for k, v in MorseCode.items():
        if v == value:
            return k


def encode_to_morse(text) -> str:
    '''Функция кодирования сообщения'''
    global MorseCode
    string = text
    output = []
    for i in string:
        temp = []
        for j in i:
            if j.upper() in MorseCode:
                temp.append(MorseCode[j.upper()])
            elif j == ' ':
                temp.append(' / ')
            else:
                temp.append(j)
        output.append(' '.join(i for i in temp))
    output = ' / '.join(i for i in output)
    return output


def decode_from_morse(text) -> str:
    '''Функция декодирования сообщения'''
    global MorseCode
    output = []
    # разделяет строку на перенос, но не на пробел
    for i in text:
        temp = []
        for j in i.split():
            if j in list(MorseCode.values()):
                temp.append(get_key(j))
            else:
                temp.append(j)
        output.append(''.join(i for i in temp))
    output = '\n'.join(i for i in output).replace('/', ' ')
    return output


def main():
    print('Программа работает только с латинским алфавитом')
    while True:
        print('Введите цифру')
        print('Вы можете \n 1 - закодировать \n 2 - декодировать\n 3 - завершить программу')
        answer = input()
        if answer == "1":
            print('Вводите текст до пустой строки:')
            text = []
            while True:
                string = input()
                if string:
                    text.append(string)
                else:
                    break
            print(text)
            encode = encode_to_morse(text)
            print('\nЗакодированный текст:\n', encode, sep='\n')
        elif answer == "2":
            print('Вводите текст до пустой строки:')
            text = []
            while True:
                string = input()
                if string:
                    text.append(string)
                else:
                    break
            decode = decode_from_morse(text)
            print('\nДекодированный текст:', decode, sep='\n')
        elif answer == "3":
            break


main()
