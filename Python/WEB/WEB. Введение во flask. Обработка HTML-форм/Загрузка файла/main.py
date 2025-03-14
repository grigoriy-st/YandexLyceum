import os
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/load_photo', methods=['GET', 'POST'])
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

