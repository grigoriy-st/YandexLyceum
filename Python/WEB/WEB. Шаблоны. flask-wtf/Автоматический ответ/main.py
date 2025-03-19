from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

last_answer = None  # Последняя сгенерирвоанная анкета


def get_random_data():
    title = ['Заголовок 1', 'Заголовок 2', 'Заголовок 3', 'И на Марсе будут яблони цвести!']
    surnames = ['Мирко', 'Лидно', 'Андор']
    names = {'Миша': 1, 'Валентин': 1, 'Женя': 0, 'Саша': 0}
    name = random.choice(list(names.keys()))

    random_data = {
        'title': random.choice(title),
        'surname': random.choice(surnames),
        'name': name,
        'education': random.choice(['Среднее', 'Высшее', 'Неполное высшее', 'Докторантура']),
        'prof': random.choice(['Инженер', 'Врач', 'Учитель', 'Программист', 'Архитектор']),
        'sex': 'Мужской' if names[name] else 'Женский',
        'motivation': random.choice(['Желание исследовать', 'Научные исследования', 'Новые возможности', 'Изоляция']),
        'ready': random.choice(['Да', 'Нет'])
    }
    return random_data


@app.route('/index/<string:title>')
def index(title):
    print('-' * 10, title)
    return render_template('base.html', 
                           title_word=title)


@app.route('/answer')
def get_answer_page():
    if not last_answer:
        text = f'''Данные анкеты ещё не сгенерированы.<br>
        Перейдите по <a href="http://127.0.0.1:8080/auto_answer">ссылке</a>,
        чтобы сгенерировать данные.'''
        return text
    return render_template('answer.html', data=last_answer)


@app.route('/auto_answer')
def generate_answer():
    global last_answer
    last_answer = get_random_data()
    text = f'''Данные по анкете успешно сгенерированы.<br>
    Можете просмотреть анкету <a href="http://127.0.0.1:8080/answer">здесь</a>'''
    return text


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')