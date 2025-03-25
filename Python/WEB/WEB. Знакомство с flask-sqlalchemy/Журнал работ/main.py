import os
import datetime
from flask import Flask, render_template, redirect, url_for, request
from sqlalchemy.exc import IntegrityError

from data import db_session
from data.users import User
from data.news import News
from data.jobs import Jobs
from forms.user import RegisterForm
from werkzeug.security import generate_password_hash

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# if 'WEB. Знакомство с flask-sqlalchemy' not in os.getcwd():
#     os.chdir('WEB. Знакомство с flask-sqlalchemy')

# class Action:
engine = create_engine('sqlite:///db/data.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
# session = Session()

# users = session.query(User).all()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run(port='8080', host="127.0.0.1")


@app.route('/')
def index():
    """ Отображение журнала работ. """
    db_sess = db_session.create_session()
    users = db_sess.query(User)
    return render_template("index.html", users=users)


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Нерабочая функция регистрации"""
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', form=form, message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', form=form, message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.hashed_password = generate_password_hash(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/')
    return render_template('register.html', form=form)


@app.route('/create_job', methods=['GET', 'POST'])
def create_job():
    """ Страница создания работы. """
    if request.method == 'POST':
        title = request.form['title']
        team_leader = request.form['team_leader']
        duration = request.form['duration']
        list_of_collaborators = request.form['list_of_collaborators']
        is_finished = request.forn['is_finished']

        new_job = Jobs(
            team_leader=team_leader,
            job=title,
            collaborators=list_of_collaborators,
            duration=duration,
            is_finished=True if is_finished == "yes" else False,
        )

        try:
            db_ss = db_session.create_session()
            db_ss.add(new_job)

        except IntegrityError:
            db_ss.rollback()
            error_message = "Ошибка при добавлении работы. Возможно, такая работа уже существует."
            return render_template('add_job.html', error=error_message)

    return render_template('new_job.html')


@app.route('/add_user')
def add_user():
    new_user = User(
        surname="Иванов",
        name="Иван",
        age=20,
        position="Разработчик",
        speciality="Программист",
        address="Москва, ул. Примерная, д. 1",
        email="ivanov@example.com"
    )

    new_user.set_password("secure_password")
    db_sess = db_session.create_session()
    db_sess.add(new_user)
    db_sess.commit()

    return "User is added!"


if __name__ == "__main__":
    main()
