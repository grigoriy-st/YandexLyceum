from data import db_session
from sources import user_reqparse
from flask import jsonify
from models.users import User
from flask_restful import abort, Api, Resource
from models.data_parser import reqparse as parser

from werkzeug.security import generate_password_hash, check_password_hash


def abort_if_user_not_found(users_id):
    session = db_session.create_session()
    users = session.query(User).get(users_id)
    if not users:
        abort(404, message=f"user {users_id} not found")


def set_password(self, password):
    self.hashed_password = generate_password_hash(password)


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        users = session.query(User).get(user_id)
        return jsonify({'users': users.to_dict(
            only=('id', 'name', 'about', 'email'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'about')) for item in user]})

    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()

        users = User(
            id=args['id'],
            name=args['name'],
            about=args['about'],
            email=args['email'],
            created_date=args['created_date']
        )
        users.set_password(args['hashed_password'])
        session.add(users)
        session.commit()
        session.close()

        return jsonify({'id': users.id})
