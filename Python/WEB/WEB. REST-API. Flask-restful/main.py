import datetime
import sqlalchemy

from flask import jsonify, Flask, render_template, redirect
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data import users_resource, news_resources
from models.news import News
from models.users import User

app = Flask(__name__)
api = Api(app)

api.add_resource(news_resources.NewsListResource, '/api/v2/news')
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')


@app.route("/")
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private is not True)
    return render_template("index.html", news=news)


@app.route('/users')
def get_users():
    db_ss = db_session.create_session()
    users = db_ss.query(User).all()

    return render_template

def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(users_resource.UsersListResource, '/api/v2/users') 

    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')


if __name__ == '__main__':
    app.run(port="8080", host="127.0.0.1")
