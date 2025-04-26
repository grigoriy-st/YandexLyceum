import datetime
import sqlalchemy
import logging

from flask import jsonify, Flask, render_template, redirect
from flask_restful import reqparse, abort, Api, Resource

from flask_login import (LoginManager, login_user,
                         login_required, logout_user,
                         current_user)

from data import db_session
from sources import users_resource, news_resources, jobs_resource
from models.news import News
from models.users import User

# Handlers
from handlers.auth import auth_bp
from handlers.work_with_jobs import work_with_jobs_bp
from handlers.work_with_departments import work_with_departments_bp
from handlers.work_with_users import work_with_users_bp

from api.jobs_api import jobs_api
from api.users_api import users_api

logging.basicConfig(level=logging.INFO)


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(work_with_users_bp)
app.register_blueprint(work_with_jobs_bp)
app.register_blueprint(work_with_departments_bp)

app.register_blueprint(jobs_api)
app.register_blueprint(users_api)

db_session.global_init("db/blogs.sqlite")

api.add_resource(news_resources.NewsListResource, '/api/v2/news')
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:id>')


@app.route("/")
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private.isnot(True)).all()  
    return render_template("index.html", news=news)


@app.route('/users')
def get_users():
    db_ss = db_session.create_session()
    users = db_ss.query(User).all()
    return render_template("users.html", users=users)  


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return 'Вы не авторизованы. Пожалуйста перейдите по <a href="/login">ссылке</a> для авторизации.'


if __name__ == '__main__':
    app.run(port="8080", host="127.0.0.1")
