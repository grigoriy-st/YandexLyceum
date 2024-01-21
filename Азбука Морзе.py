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

def get_key(value):
    '''Функция поиска буквы в словаре(по значению)'''
    global MorseCode
    for k, v in MorseCode.items():
        if v == value:
            return k

def encode_to_morse(text):
    '''Функция кодирования сообщения'''
    global MorseCode
    string = text.split()
    output = []
    for i in string:
        temp = []
        for j in i:
            if j.upper() in MorseCode:
                temp.append(MorseCode[j.upper()])
            else:
                temp.append(j)
        output.append(' '.join(i for i in temp))
    output = '\n'.join(i for i in output)
    return output


def decode_from_morse(text):
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
    output = ' '.join(i for i in output)
    return output

def main():
    print('Программа работает только с латинским алфавитом')
    while True:
        answer = input('Вы хотите "закодировать", "декодировать"')
        if answer == "закодировать":
            text = input('Введите текст:\n')
            encode = encode_to_morse(text)
            print('\nЗакодированный текст:\n', encode, sep='\n')
        elif answer == "декодировать" or answer == '2':
            text = []
            print('Вводите текст до пустой строки:')
            while True: # Цикл для ввода многострочного текста
                line = input()
                if not line:
                    break
                text.append(line)
            decode = decode_from_morse(text)
            print('\nДекодированный текст:', decode.capitalize(), sep='\n')
        else:
            print('\n\nЕсли хотите продолжить напишите "да"')
            print('Чтобы закончить программу нажмите Enter')
            if input():
                continue
            break


main()