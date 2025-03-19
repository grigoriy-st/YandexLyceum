ru_alfb = [chr(i) for i in range(ord('А'), ord('Я') + 1)]
en_alfb = [chr(i) for i in range(ord('A'), ord('Z') + 1)]


def its_combination(password):
    std_en_layout = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
    std_ru_layout = ['йцукенгшщзхъ', 'фывапролджэё', 'ячсмитьбю']

    password = password.lower()
    for lets_3 in range(len(password)):

        word = password[lets_3:lets_3 + 3]
        if len(word) == 3 and word.isalpha():

            for string in std_en_layout:
                for seq in range(len(string)):
                    if word == string[seq:seq + 3]:
                        return True

            for string in std_ru_layout:
                for seq in range(len(string)):
                    if word == string[seq:seq + 3]:
                        return True
    return False


class PasswordError(ValueError):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


class SequenceError(PasswordError):
    pass


def check_password(password):
    try:

        if len(password) < 9:
            raise LengthError()

        if password.lower() == password or password.upper() == password:
            raise LetterError()

        if not (set(password) & set('1234567890')):
            raise DigitError()

        if its_combination(password):
            raise SequenceError()

    except Exception as error:
        return error.__class__.__name__
    else:
        return 'ok'