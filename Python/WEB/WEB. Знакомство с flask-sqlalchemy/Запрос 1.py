import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base
import datetime

SqlAlchemyBase = declarative_base()


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)


db_name = input().strip()

engine = sqlalchemy.create_engine(f'sqlite:///{db_name}')
Session = sessionmaker(bind=engine)
session = Session()

colonists = session.query(User.id).filter(
    User.address == 'module_1',
    ~User.position.ilike('%engineer%'),
    ~User.speciality.ilike('%engineer%')
).all()

for colonist_id, in colonists:
    print(colonist_id)

session.close()
