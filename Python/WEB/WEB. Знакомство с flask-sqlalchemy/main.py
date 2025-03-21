from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
from data import db_session

def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
