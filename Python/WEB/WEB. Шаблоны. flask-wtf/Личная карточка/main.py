import json
import flask
import random
from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/member')
def get_member_page():
    with open('static/json/data.json', 'r') as file:
        data = json.load(file)

    random_member = random.choice(data)
    random_member['specialties'].sort()
    return render_template('index.html', data=random_member)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
