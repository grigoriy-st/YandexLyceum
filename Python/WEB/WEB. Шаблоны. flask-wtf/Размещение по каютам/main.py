from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/distribution')
def get_page():
    data = {
        "austronaut_list": [
            "Ридли Скотт",
            "Энди Уир",
            "Марк Уотни",
            "Венката Капут",
            "Тедди Сандерс",
            "Шон Бин",
        ],
    }
    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')