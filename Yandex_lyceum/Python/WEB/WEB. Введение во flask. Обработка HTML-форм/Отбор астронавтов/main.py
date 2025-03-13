from flask import Flask, url_for, request, render_template

app = Flask(__name__)
@app.route('/choice/<planet_name>', methods=['POST', 'GET'])
def get_pae(planet_name):
    specialities = ['Инженер-исследователь', 'Инженер-строитель', 
                    'Пилот', 'Метеоролог', 'Инженер по жизнеобеспечению', 
                    ' Инженер по радиационной защите',
                    'Врач', 'Экзлбиолог']
    
    return render_template('index.html')
    
    if request.method == 'GET':
        return f'''<!doctype html>
                        '''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"
    

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

