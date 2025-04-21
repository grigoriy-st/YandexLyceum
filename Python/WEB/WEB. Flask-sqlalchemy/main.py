# main.py

# Этот файл скорее всего есть в репозитории
# https://github.com/grigoriy-st/YandexLyceum/tree/main/Python/WEB

import datetime
import sqlalchemy
from flask import Flask, request, redirect, abort
from flask_login import (LoginManager, login_user,
                         login_required, logout_user,
                         current_user)
from data import db_session
from data.users import User
from data.news import News
from data.jobs import Jobs

from forms.user import RegisterForm
from forms.NewsForm import NewsForm
from forms.LoginForm import LoginForm
from flask import render_template, redirect

from werkzeug.security import generate_password_hash

# Handlers
from handlers.auth import auth_bp
from handlers.work_with_jobs import work_with_jobs_bp
from handlers.work_with_departments import work_with_departments_bp
from api.jobs_api import jobs_api
from api.users_api import users_api
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

app.register_blueprint(auth_bp)
app.register_blueprint(work_with_jobs_bp)
app.register_blueprint(work_with_departments_bp)
app.register_blueprint(jobs_api)
app.register_blueprint(users_api)

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/blogs.db")
    app.run(port='8080', host="127.0.0.1")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return 'Вы не авторизованы. Пожалуйста перейдите по <a href="/login">ссылке</a> для авторизации.'


@app.route('/')
def get_main_page():
    return render_template('user_list.html')


@app.route('/user_list')
def get_user_list():
    """ Отображение списка пользователей. """

    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return render_template('user_list.html', users=users)


if __name__ == '__main__':
    main()
