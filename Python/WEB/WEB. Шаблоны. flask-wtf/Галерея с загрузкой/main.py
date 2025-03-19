import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/galery', methods=['GET', 'POST'])
def get_carousel_page():
    current_index = 0
    images = os.listdir('static/img')

    if request.method == 'POST':
        print(request.form)
        if 'next' in request.form:
            current_index = (int(request.form['current_index']) + 1) % len(images)
        elif 'prev' in request.form:
            current_index = (int(request.form['current_index']) - 1) % len(images)
        elif 'upload_photo' in request.form:
            file = request.files['file']
            if file.filename == '':
                return redirect(request.url)
            if file:
                filename = file.filename
                file.save(os.path.join('static/img', filename))

    return render_template('index.html', images=images, current_index=current_index)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
