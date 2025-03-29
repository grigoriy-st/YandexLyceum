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
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        db_ss = db_session.create_session()
        user = db_ss.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template("login.html",
                               message="Error",
                               form=form)
    return render_template('login.html', title='Authorization', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


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


@app.route('/register', methods=['GET', 'POST'])
def register():
    """ Регистрация пользователя. """
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   form=form,
                                   message="Пароли не совпадают")

        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html',
                                   form=form,
                                   message="Такой пользователь уже есть")

        user = User(
            email=form.email.data,
            surname=form.surname.data,
            name=form.name.data,
            age=form.age.data,
            position=form.position.data,
            speciality=form.speciality.data,
            address=form.address.data,
        )
        user.hashed_password = generate_password_hash(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return render_template('register.html',
                               form=form, message="The user has been added")

    return render_template('register.html', form=form)


@app.route('/create_job', methods=['GET', 'POST'])
def create_job():
    """ Страница создания работы. """
    db_ss = db_session.create_session()

    # Получение всех пользователей
    team_leaders = db_ss.query(User).all()

    if request.method == 'POST':
        title = request.form['title']
        team_leader = request.form['team_leader']
        beginning_of_duration = request.form['beginning_of_duration']
        end_of_duration = request.form['end_of_duration']
        list_of_collaborators = request.form['list_of_collaborators']
        is_finished = request.form['is_finished']

        # Вычисление разницы времени
        start_date = datetime.strptime(beginning_of_duration, "%Y-%m-%dT%H:%M")
        end_date = datetime.strptime(end_of_duration, "%Y-%m-%dT%H:%M")
        difference = end_date - start_date
        days_difference = difference.days
        seconds_difference = difference.seconds

        work_size = days_difference * 24 + seconds_difference // 3600

        # Работа с бд

        new_job = Jobs(
            team_leader=team_leader,
            job=title,
            collaborators=list_of_collaborators,
            start_date=start_date,
            end_date=end_date,
            work_size=work_size,
            is_finished=True if is_finished == "finished" else False,
        )

        try:
            db_ss.add(new_job)
            db_ss.commit()
            message = "Job is added"

        except IntegrityError as e:
            print(f"Error: {e}")
            db_ss.rollback()
            error_message = "Ошибка при добавлении работы. " \
                            "Возможно, такая работа уже существует."

            return render_template('new_job.html',
                                   error=error_message,
                                   team_leaders=team_leaders)

        return render_template('new_job.html',
                               message=message,
                               team_leaders=team_leaders)

    return render_template('new_job.html', team_leaders=team_leaders)


@app.route('/user_list')
def get_user_list():
    """ Отображение списка пользователей. """

    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return render_template('user_list.html', users=users)


if __name__ == '__main__':
    main()
