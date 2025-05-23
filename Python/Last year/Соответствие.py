'''
Если у вас есть много данных, то можно попытаться описать их какой-либо функцией.
Если такую функцию найти, то можно предугадать тренд изменения поведения ваших
данных в будущем. И много еще полезного несет знание такой функции.

Напишите функцию trend(), определяющую, подходит ли некоторая зависимость к имеющимся данным.

Функция принимает произвольное число кортежей (значение аргумента x, значение
функции), и то и другое – вещественные числа. Также функция принимает произвольное
число именованных аргументов – это функции для проверки. Если какая-то из функций
настолько хорошо описывает ваши данные, что отклонение всех результатов при подстановке
x в функцию не превышает 0.01, то нужно вернуть имя именованного аргумента, в который
записана эта функция. Если ничего подходящего не нашлось, вернуть None.
'''

def trend(*data, **functions):
    m_res = [x[1] for x in data]
    for f in functions:
        t = list(map(functions[f], [x[0] for x in data]))
        temp = []
        for i in range(len(data)):
            if -1 < float(t[i]) - float(m_res[i]) <= 0.001:
                temp.append(1)
        if len(temp) == len(data):
            return f


data = [(0, 2.0), (-1.0, 3.05), (3.0, -1), (-2.0, 4.0), (18, -16.001)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3,
             "line_1": lambda x: -x + 2}
print(trend(*data, **functions))
data = [(0, 0), (-1.0, 1.001), (3.0, 8.999), (-2.0, 4.0)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3}
print(trend(*data, **functions))
data = [(0, 0), (-1.0, -3.01), (3.0, 9.0), (-2.0, -6.0)]
functions = {"line": lambda x: 3 * x,
             "square": lambda x: x ** 2,
             "cube": lambda x: 0.5 * x ** 3}
print(trend(*data, **functions))

