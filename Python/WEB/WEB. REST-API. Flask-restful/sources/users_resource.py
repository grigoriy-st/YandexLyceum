from data import db_session
from parsers import users_parser
from flask import jsonify
from models.users import User
from flask_restful import abort, Api, Resource

from flask_restful.reqparse import RequestParser
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash


def abort_if_user_not_found(users_id):
    try:
        session = db_session.create_session()
        users = session.query(User).filter(User.id == users_id).first()
        if not users:
            abort(404, message=f"user {users_id} not found")
    finally:
        session.close()


def set_password(self, password):
    self.hashed_password = generate_password_hash(password)


class UsersResource(Resource):
    def get(self, user_id):
        """ Получение информации по одному пользователю. """
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        session.close()
        return {'user': {
            'id': user.id,
            'name': user.name,
            'position': user.position,
            'email': user.email
        }}

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id).first()
        session.delete(user)
        session.commit()
        session.close()
        return {'success': 'OK'}


class UsersListResource(Resource):
    def get(self):
        session = db_session.create_session()
        try:
            users = session.query(User).all()
            user_list = []
            for user in users:        
                user_list.append({
                    'id': user.id, 
                    'name': user.name, 
                    'position': user.position
                })
            return {'users': user_list}
        except Exception as e:
            return {'status': 'error', 'message': str(e)}, 500
        finally:
            session.close()

    def post(self):
        parser = users_parser.create_user_parser()
        args = parser.parse_args()

        session = db_session.create_session()
        try:
            founded_user = session.query(User).filter(User.id == args['id']).first()

            if founded_user:
                return {
                    'status': 'error',
                    'message': 'User with this ID already exists'
                }, 400

            password = args['hashed_password']

            if not password:
                return {
                    'status': 'error',
                    'message': 'User doesn\'t have a password'
                }, 400

            user = User(
                id=args['id'],
                name=args['name'],
                position=args['position'],
                email=args['email'],
                modified_date=args['modified_date']
            )
            user.set_password(password)
            session.add(user)
            session.commit()

            return {
                'status': 'success',
                'id': f'{user.id}'
            }, 201
        except SQLAlchemyError as e:
            session.rollback()
            return {
                'status': 'error',
                'message': str(e)
            }, 400
        finally:
            session.close()