from flask_restful.reqparse import RequestParser


def create_user_parser():
    parser = RequestParser()
    parser.add_argument('id')
    parser.add_argument('name')
    parser.add_argument('position')
    parser.add_argument('email')
    parser.add_argument('modified_date')
    parser.add_argument('hashed_password')

    return parser

user_parser = create_user_parser()