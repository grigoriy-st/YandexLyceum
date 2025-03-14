import flask
from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/list_prof/<list_type>')
def get_page_by_spec(list_type: str):
    if list_type not in ['ol', 'ul']:
        return "Ошибка в url"

    data = {
        "list_type": list_type,
        "profs": [
            'инженер-исследователь',
            'пилот',
            'строитель',
            'экзобиолог',
            'врач',
            'инженер по терраформированию',
            'климатолог',
            'специалист по радиационной защите',
            'астрогеолог',
            'глянциолог',
            'инженер жизнеобеспечения',
            'метеоролог',
            'оператор марсохода',
            'киберинженер',
            'штурман',
            'пилот дронов',
        ]
    }
    
    return render_template('index.html', page=data)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
