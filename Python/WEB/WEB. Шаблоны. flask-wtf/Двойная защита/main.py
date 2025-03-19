from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def get_pae():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
