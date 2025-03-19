from flask import Flask
from flask import render_template, request, url_for

app = Flask(__name__)


@app.route('/table/<sex>/<int:age>')
def get_page(sex, age):
    wall_color = image = None

    if sex == 'male' and age >= 21:
        wall_color = 'blue'
        image = 'adult.png'
    elif sex == 'male' and age < 21:
        wall_color = 'rgb(65, 255, 255)'
        image = 'young.png'
    elif sex == 'female' and age >= 21:
        wall_color = 'orange'
        image = 'adult.png'
    elif sex == 'female' and age < 21:
        wall_color = 'sandybrown'
        image = 'young.png'

    data = {
        'image': image,
        'wall_color': wall_color,
    }

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')