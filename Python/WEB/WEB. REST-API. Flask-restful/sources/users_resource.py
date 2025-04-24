from data import db_session
from sources import user_reqparse
from flask import jsonify
from models.users import User
from flask_restful import abort, Api, Resource

from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import IntegrityError
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
            only=('id', 'name', 'position', 'email'))})

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
            only=('id', 'name', 'position')) for item in user]})

    def post(self):
        parser = RequestParser()
        parser.add_argument('id')
        parser.add_argument('name')
        parser.add_argument('position')
        parser.add_argument('email')
        parser.add_argument('modified_date')
        parser.add_argument('hashed_password')

        args = parser.parse_args()
        try:
            session = db_session.create_session()

            users = User(
                id=args['id'],
                name=args['name'],
                position=args['position'],
                email=args['email'],
                modified_date=args['modified_date']
            )
            users.set_password(args['hashed_password'])
            session.add(users)
            session.commit()
            return jsonify({
                'status': 'success',
                'id': users.id}
            )
        except IntegrityError as e:
            session.rollback()
            return jsonify({
                'status': 'error',
                'message': e,
            })
        finally:
            session.close()
