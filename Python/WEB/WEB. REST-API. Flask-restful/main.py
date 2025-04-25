import datetime
import sqlalchemy

from flask import jsonify, Flask, render_template, redirect
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from sources import users_resource, news_resources, jobs_resource
from models.news import News
from models.users import User

app = Flask(__name__)
api = Api(app)


db_session.global_init("db/blogs.sqlite")  

api.add_resource(news_resources.NewsListResource, '/api/v2/news')
api.add_resource(news_resources.NewsResource, '/api/v2/news/<int:news_id>')
api.add_resource(users_resource.UsersListResource, '/api/v2/users')
api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:user_id>')
api.add_resource(jobs_resource.JobsListResource, '/api/v2/jobs')
api.add_resource(jobs_resource.JobsResource, '/api/v2/jobs/<int:jobs_id>')

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


if __name__ == '__main__':
    app.run(port="8080", host="127.0.0.1")