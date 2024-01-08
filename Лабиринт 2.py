from datetime import datetime, timedelta
seconds = 121
#start = datetime.now()
#end = start + timedelta(minutes=2)
#def check_time():
#    '''Функция для проверки текущего времени 
#    с временем приезда полиции'''
#    if datetime.now() > end:
#        print(' False ')
#    else:
#        print(' True ')
print(
    "Вы грабитель банка. Вам необходимо скрыться",
    f"от полиции поднявшись наверх здания.\nТам вас будет ожидать вертолёт.",
    'Выбирайте только действия, которые есть в кавычках. Слова регистрозависимые.'
)
print('-' * 15,'Игра началась', '-' * 15)
paths = {
    0: ["оставить 50000$", "выйти", "взять ещё 50000$"],
    1: {
        'кабинет охранника': ['взять ключ от серверного шкафа', "выключить камеры", 'выйти'],
        'кабинет секретаря': ['прочитать записку', "выйти"],
        'серверную': ['удалить записи с камер', 'ввести код-пароль','выйти']},
        'второй этаж': ['подняться', 'спуститься'],
    2:{'дверь в конце коридора': ['подняться на лифте', 'подняться по лестнице']}
     }
items = {
    'key': False,
    'cameras': False,
    'del_video':False,
    'kod_pass':False,
}
not_free = True
pos = 0
money = 100000
money_bank = 400000
act_1lvl = ''
while not_free:
    if pos == 0:
        print(f"Вы находитесь в хранилище с деньгами.\
            \nВы можете {paths[pos]}")
        answer = input("Выберите действие: ")
        while answer not in paths[0]:
            print('Вы ввели неправильную команду')
            answer = input("Выберите действие: ")
        if answer == "взять ещё 50000$":
            if money_bank >= 50000:
                money += 50000
                money_bank -= 50000
                print(f'Вы взяли ещё 50000$. Ваш баланс: {money}')
            else:
                print(f'В банке ничего нет. Ваш баланс: {money}')
        elif answer == "оставить 50000$":
            if money_bank >= 50000:
                if money == 0:
                    print('На вашем балансе 0. Вам нечего оставлять.')
                else:
                    money -= 50000
                    money_bank += 50000
                    print(f'Вы оставили 50000$ в хранилище банк.\
                        Ваш баланс: {money}')
            else:
                print('В банке ничего нет')
        elif answer == 'выйти':
            pos += 1
            continue
    if pos == 1:
        rooms = list(paths[pos].keys())
        print(f"Вы находитесь на втором этаже\
            \nВы можете зайти в {rooms}")
        room = input('В какую комнату хотите попасть: ')
        while room not in paths[pos].keys():
            print('Такой комнаты нет')
            room = input('В какую комнату хотите попасть: ')
        if room == rooms[0]:
            action = ''
            while action != 'выйти':
                print('Вы в кабинете охранника.')
                print(f'Вы можете {paths[pos][room]}')
                action = input('Введите действие: ')
                while action not in paths[pos][room]:
                    print('Такого действия нет')
                    action = input('Введите действие: ')
                if action == 'взять ключ от серверного шкафа':
                    items['key'] = True
                    print('Ключ у вас!')
                    continue
                elif action == "выключить камеры":
                    items['cameras'] = True
                    print('Камеры отключены!')
                    continue
                elif action == 'Выйти':
                    continue
        if room == rooms[1]:
            action = ''
            while action != 'выйти':
                print('Вы в кабинете секретаря.')
                print(f'Вы можете {paths[pos][room]}')
                action = input()
                if action == 'прочитать записку':
                    items['kod_pass'] = True
                    print('Из записки вы узнали КОД-ПАРОЛЬ от серверной')
                elif action == 'Выйти':
                    continue
        if room == rooms[2]:
            action1 = ''
            while action1 != 'выйти':
                access = False  # проверка на доступ к серверной
                suc_count = 0
                kod_pass = False    # проверка наличие пароля
                if items['key']:
                    print('Вы в серверной.')
                    print(f'Ваши действия: {paths[pos][room]}')
                    action1 = input('Введите действие: ')
                    while action1 not in paths[pos][room]:
                        print('Такого действия нет')
                        action1 = input('Введите действие: ')
                    for i in items:
                            if items[i] == True:
                                suc_count += 1
                            else:
                                if i == 'key':
                                    print('У вас отсутствует ключ от серверного шакафа')
                                if i == 'kod_pass':
                                    print('У вас отсутствует код-пароль')
                                if i == 'cameras':
                                    print('Вы не отключили камеры. Вас точно поймают.')
                                action = 'выйти'
                                continue
                    if action1 == 'удалить записи с камер':
                        if suc_count == 3:
                            access = True
                        if access:
                            print('Записи с камер успешно удалены!')
                                   
                        else:
                            print('У вас нет КОД-ПАРОЛЯ от серверной')
                            print('Вернитесь в кабинет секретаря. Код написан на записке.')
                            response = input('Вы вернуться в кабинет секретаря? "да" / "нет"')
                            if response == 'да':
                                room = rooms[0]
                                continue
                            else:
                                continue
                    elif action1 == 'ввести код-пароль':
                        if access:
                            kod_pass = True
                            print('КОД-ПАРОЛЬ введён!')
                            print('Сигнализация отключена!')
                            continue
                        else:
                            print('У вас нет доступа для ввода КОД-ПАРОЛЯ!')
                            continue
                    elif action1 == 'Выйти':
                        continue
                else:
                    print('У вас нет ключа от серверного шкафа!')
                    print('Ключ находится в кабинете охранника.')
                    response = input('Вы хотите вернуться в кабинет охранника? "да" / "нет"')
                    if response == 'да':
                        action1 = 'выйти'
                        continue
                    else:
                        continue
                
                