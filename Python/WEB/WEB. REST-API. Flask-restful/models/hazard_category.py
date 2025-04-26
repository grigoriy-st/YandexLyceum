import datetime
import sqlalchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.users import SqlAlchemyBase


class HazardCategory(SqlAlchemyBase):
    __tablename__ = 'hazard_category'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True,
                           autoincrement=True)
    hazard_category_title = sqlalchemy.Column(sqlalchemy.String)

    jobs = relationship("Jobs", back_populates='hazard_category_rel')