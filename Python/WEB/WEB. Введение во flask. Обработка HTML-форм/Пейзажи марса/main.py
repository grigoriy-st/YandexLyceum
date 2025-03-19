import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/galery', methods=['GET', 'POST'])
def get_carousel_page():
    current_index = 0
    images = os.listdir('static/img')
    print('Фото в папке:', images)
    if request.method == 'POST':
        if 'next' in request.form:
            current_index = (int(request.form['current_index']) + 1) % len(images)
        elif 'prev' in request.form:
            current_index = (int(request.form['current_index']) - 1) % len(images)

    return render_template('index.html', images=images, current_index=current_index)

def upload_file():
    filename = None
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = file.filename
            file.save(os.path.join('static/img', filename))
            return redirect(url_for('upload_file', filename=filename))

    filename = request.args.get('filename')
    return render_template('index.html', filename=filename)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
