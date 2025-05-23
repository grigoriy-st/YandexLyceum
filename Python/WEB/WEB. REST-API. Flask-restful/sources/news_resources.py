from flask import jsonify, abort
from flask_restful import Resource, reqparse
from data import db_session
from models.news import News
from parsers import users_parser


class NewsResource(Resource):
    def get(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        session.close()

        return jsonify({
            'news': news.to_dict(
                only=('title', 'content', 'user_id', 'is_private')
            )
        })

    def delete(self, news_id):
        abort_if_news_not_found(news_id)
        session = db_session.create_session()
        news = session.query(News).get(news_id)
        session.delete(news)
        session.commit()
        session.close()

        return jsonify({'success': 'ok'})


class NewsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(News).all()
        session.close()

        return jsonify({
            'news': [item.to_dict(
                only=('title', 'content', 'user.name')) for item in news ]
        })

    def post(self):
        parser = users_parser.create_user_parser()
        args = parser.parse_args()

        try:
            session = db_session.create_session()
            news = News(
                title=args['title'],
                content=args['content'],
                user_id=args['user_id'],
                is_published=args['is_published'],
                is_private=args['is_private'],
            )
            session.add(news)
            session.commit()

            return jsonify({'id': news.id})
        finally:
            session.close()


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    session.close()

    if not news:
        abort(404, message=f"News {news_id} not found")
