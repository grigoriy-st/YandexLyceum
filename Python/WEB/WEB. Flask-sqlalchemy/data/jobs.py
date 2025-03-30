# jobs.py

# Этот файл скорее всего есть в репозитории
# https://github.com/grigoriy-st/YandexLyceum/tree/main/Python/WEB

import datetime
import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from data.users import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    ForeignKey('users.id'), nullable=False)
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)

    team_leader_user = relationship("User", backref='jobs')
