import datetime
import sqlalchemy

from flask import jsonify, Flask, render_template, redirect
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data import users_resource

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


def main():
    db_session.global_init("db/blogs.db")
    api.add_resource(users_resource.UsersListResource, '/api/v2/users') 

    api.add_resource(users_resource.UsersResource, '/api/v2/users/<int:users_id>')


if __name__ == '__main__':
    app.run(port="8080", host="127.0.0.1")