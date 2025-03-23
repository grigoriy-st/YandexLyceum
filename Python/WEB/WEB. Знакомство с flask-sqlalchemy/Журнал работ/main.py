import os
from flask import Flask, render_template, redirect
from data import db_session
from data.users import User
from data.news import News
from forms.user import RegisterForm
from werkzeug.security import generate_password_hash

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# if 'WEB. Знакомство с flask-sqlalchemy' not in os.getcwd():
#     os.chdir('WEB. Знакомство с flask-sqlalchemy')

# class Action:
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run(port='8080', host="127.0.0.1")


@app.route('/')
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


@app.route('/register', methods=['GET', 'POST'])
def register():
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


if __name__ == "__main__":
    main()