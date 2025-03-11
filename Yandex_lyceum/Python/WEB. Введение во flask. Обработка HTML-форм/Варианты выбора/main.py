from flask import Flask, url_for, request, render_template

app = Flask(__name__)
@app.route('/choice/<planet_name>', methods=['POST', 'GET'])
def get_pae(planet_name):
    return render_template('intex.html', item=planet_name)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

