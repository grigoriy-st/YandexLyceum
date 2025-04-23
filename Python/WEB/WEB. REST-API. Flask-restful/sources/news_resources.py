from flask import jsonify, abort
from flask_restful import Resource, reqparse
from data import db_session
from models.news import News


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

    def delte(self, news_id):
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

    def get_post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('content', required=True)
        parser.add_argument('is_private', required=True, type=bool)
        parser.add_argument('is_published', required=True, type=bool)
        parser.add_argument('user_id', required=True, type=int)

        args = parser.parse_args()
        session = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_publishied=args['is_pblished'],
            is_private=args['is_private'],
        )
        session.add(news)
        session.commit()
        session.close()

        return jsonify({'id': news.id})


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(News).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")
