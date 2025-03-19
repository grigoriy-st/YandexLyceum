from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/index')
def index():
    return "Миссия Колонизация Марса"


@app.route('/')
def get_text():
    return "И на Марсе будут яблони цвести!"

@app.route('/promotion')
def get_promotion():
    text = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]
    return '<br>'.join(text)

@app.route('/image_mars')
def image():
    return f'''
			<title>Привет, Марс!</title>
			<h2>Жди нас, марс!</h2>
                <img width=300px height=300px src="{url_for('static', filename='mars.jpg')}" 
           alt="Изображение марса">
           <p>Вот она какая, красная планета!</p>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')