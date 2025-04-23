import datetime
import sqlalchemy
from sqlalchemy import orm

from data.db_session import SqlAlchemyBase


class News(SqlAlchemyBase):
    __tablename__ = 'news'

    id = sqlalchemy.Column(sqlalchemy.Integer, 
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    content = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, 
                                     default=datetime.datetime.now)
    is_private = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    user_id = sqlalchemy.Column(sqlalchemy.Integer, 
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship("User", back_populates="news")
    is_published = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    def to_dict(self, only=None):
        """Преобразует объект в словарь."""
        result = {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'is_private': self.is_private,
            'is_published': self.is_published,
            'user_id': self.user_id,
        }
        if only:
            return {key: result[key] for key in only if key in result}
        return result