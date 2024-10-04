def success(login):
    print(f'Привет, {login}!')


def failure(login, reason):
    print(f'Кто-то пытался притвориться пользователем {login.lower()}, '
          f'но в пароле допустил ошибку: {reason.upper()}.')


def ask_password(login, password, success=None, failure=None):
    vows = set('a,e,i,o,u,y'.split(','))
    cons = set('b, c, d, f, g, h, j, k, l, m, '
               'n, p, q, r, s, t, v, w, x, z'.split(', '))
    check_vow = [i for i in password if i in vows]
    temp = [i.lower() for i in login if i in cons]
    check_cons = [i.lower() for i in password if i in cons] == temp
    if len(check_vow) == 3 and check_cons:
        if success:
            # Сделай так, чтобы эта проверка работала
            print(success)
        else:
            success(login.lower())
    else:
        if len(check_vow) != 3 and not check_cons:
            reason = 'Everything is wrong'
        elif not check_cons:
            reason = 'Wrong consonants'
        else:
            reason = "Wrong number of vowels"
        if failure:
            failure
        else:
            failure(login, reason)


def main(login, password):
    ask_password(login, password, success, failure)


ask_password("anastasia", "nsyatos", lambda login: print('super'), lambda login, err: print('bad'))