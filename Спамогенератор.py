def encrypt_caesar(msg, shift=3):
    num, string = shift, msg
    output = ''
    for i in range(len(string)):
        if 1040 <= ord(string[i]) <= 1072 or 1071 <= ord(string[i]) <= 1103:
            symbol = ord(string[i]) + num
            if string[i].isupper() and symbol > 1071:
                output += chr(1040 + (symbol - 1072))
            elif string[i].islower() and symbol > 1103:
                output += chr(1071 + (symbol - 1103))
            else:
                output += chr(symbol)
        else:
            output += string[i]
    return output


def decrypt_caesar(encrypted, shift=3):
    num, string = shift, encrypted

    output = ''
    for i in range(len(string)):
        if 1040 <= ord(string[i]) <= 1072 or 1071 <= ord(string[i]) <= 1103:
            symbol = ord(string[i]) - num
            if string[i].isupper() and symbol > 1071:
                output += chr(1040 + (symbol - 1072))
            elif string[i].islower() and symbol > 1103:
                output += chr(1071 + (symbol - 1103))

        else:
            output += string[i]
    return output
msg = "И не Цезарь, тоже привет."
encrypted = encrypt_caesar(msg, shift=54)
decrypted = decrypt_caesar(encrypted, shift=54)
print(encrypted)
print(decrypted)