import datetime
from datetime import datetime

from flask import (Blueprint, render_template,
                   redirect, request, abort,
                   url_for, flash, get_flashed_messages
                   )
from flask_login import login_user, logout_user, login_required, current_user

from forms.NewsForm import NewsForm

from data import db_session
from models.users import User
from models.jobs import Jobs
from models.news import News

from data.db_session import create_session
from sqlalchemy.exc import IntegrityError

work_with_news_bp = Blueprint('work_with_news', __name__)


@work_with_news_bp.route('/news',  methods=['GET', 'POST'])
@login_required
def add_news():
    """ НЕ РЕАЛИЗОВАНО | Добавление новости. """

    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.work_with_news_bpend(news)
        db_sess.merge(current_user)
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости', 
                           form=form)


@work_with_news_bp.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    """ НЕ РЕАЛИЗОВАНО | Редактирование новости. """
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


@work_with_news_bp.route('/news_delete/<int:id>', methods=['GET', 'POST'])
@login_required
def news_delete(id):
    """ НЕ РЕАЛИЗОВАНО | Удаление новости. """
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

