from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route('/results/<nickname>/<int:level>/<float:rating>', 
           methods=['POST', 'GET'])
def get_page(nickname, level, rating):
    items = {
        "nickname": nickname,
        "level": level,
        "rating": rating,
    }
    return render_template('index.html', items=items)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

