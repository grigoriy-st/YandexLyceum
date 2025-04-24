from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('name')
parser.add_argument('email', type=bool)