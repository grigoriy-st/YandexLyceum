# departments.py

import sqlalchemy
from sqlalchemy import orm, ForeignKey
from sqlalchemy.orm import relationship

from .db_session import SqlAlchemyBase


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('users.id'),
                              nullable=True)
    members = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    dep_email = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    chief_user = relationship("User", backref='dep_chief', foreign_keys=[chief])
