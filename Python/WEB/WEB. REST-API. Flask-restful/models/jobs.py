# jobs.py

# Этот файл скорее всего есть в репозитории
# https://github.com/grigoriy-st/YandexLyceum/tree/main/Python/WEB

import datetime
import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from data.users import SqlAlchemyBase
from data.hazard_category import HazardCategory

class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    author = sqlalchemy.Column(sqlalchemy.Integer,
                               ForeignKey('users.id'), nullable=False)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    ForeignKey('users.id'), nullable=False)
    job_title = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    hazard_category = sqlalchemy.Column(sqlalchemy.Integer,
                                        ForeignKey('hazard_category.id'),
                                        nullable=None)

    team_leader_user = relationship("User", backref='team_leader_jobs',
                                    foreign_keys=[team_leader])
    author_user = relationship("User", backref='author_jobs',
                               foreign_keys=[author])
    hazard_category_rel = relationship("HazardCategory", back_populates="jobs") 