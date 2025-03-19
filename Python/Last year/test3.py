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
        'кабинет охранника': ['взять ключ от серверной', "выключить камеры", 'выйти'],
        'кабинет секретаря': ['прочитать записку', "выйти"],
        'серверную': ['удалить записи с камер', 'ввести код-пароль','выйти']},
        'второй этаж': ['подняться', 'спуститься'],
    2:{'дверь в конце коридора': ['подняться на лифте', 'подняться по лестнице']}
     }
items = {
    'key': False,
    'cameras': False,
    'note':False,
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
            print('Вы в кабинете охранника.')
            print(f'Вы можете {paths[pos][room]}')
            action = input('Введите действие: ')
            while action not in paths[pos][room]:
                print('Такого действия нет')
                action = input('Введите действие: ')
            if action == 'взять ключ от серверной':
                items['key'] = True
            elif action == "выключить камеры":
                items['cameras'] = True
            elif action == 'Выйти':
                continue
        if room == rooms[1]:
            print('Вы в кабинете охранника.')
            print(f'Вы можете {paths[pos][room]}')
            action = input()
            if action == 'прочитать записку':
                items['note'] = True
            elif action == 'Выйти':
                continue
        if room == rooms[2]:
            if 
            print('Вы в кабинете охранника.')
            print(f'Вы можете {paths[pos][room]}')
            action = input()
            if action == 'прочитать записку':
                items['note'] = True
            elif action == 'Выйти':
                continue
    