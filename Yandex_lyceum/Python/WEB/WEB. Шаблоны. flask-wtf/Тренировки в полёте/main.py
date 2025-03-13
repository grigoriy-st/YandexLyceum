import flask
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/training/<prof>')
def get_page_by_spec(prof: str):
    prof = prof.lower()
    data = {
        "title": "Научные симуляторы",
        "image": "img/science_image.jpg"
    }
    if 'инженер' in prof or 'строитель' in prof:
        data['title'] = 'Инженерные тренажёры'
        data['image'] = 'img/engineer_image.jpg'

    return render_template('index.html', page=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')