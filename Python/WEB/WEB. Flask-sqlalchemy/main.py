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

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

app.register_blueprint(auth_bp)
app.register_blueprint(work_with_jobs_bp)

login_manager = LoginManager()
login_manager.init_app(app)


def main():
    db_session.global_init("db/blogs.db")
    app.run(port='8080', host="127.0.0.1")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def get_main_page():
    return render_template('user_list.html')


@app.route('/news',  methods=['GET', 'POST'])
@login_required
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости', 
                           form=form)


@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    form = NewsForm()
    if request.method == "GET":
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user
                                          ).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
    return render_template('news.html',
                           title='Редактирование новости',
                           form=form
                           )


@app.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.id == id,
                                      News.user == current_user
                                      ).first()
    if news:
        db_sess.delete(news)
        db_sess.commit()
    else:
        abort(404)
    return redirect('/')


@app.route('/user_list')
def get_user_list():
    """ Отображение списка пользователей. """

    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return render_template('user_list.html', users=users)


if __name__ == '__main__':
    main()
