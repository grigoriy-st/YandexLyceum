import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

images = [
    'img/first.jpg',
    'img/second.jpg',
    'img/third.jpg',
]

@app.route('/carousel', methods=['GET', 'POST'])
def get_carousel_page():
    current_index = 0
    if request.method == 'POST':
        if 'next' in request.form:
            current_index = (int(request.form['current_index']) + 1) % len(images)
        elif 'prev' in request.form:
            current_index = (int(request.form['current_index']) - 1) % len(images)
    return render_template('index.html', images=images, current_index=current_index)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

