import sqlalchemy
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine

SqlAlchemyBase = declarative_base()
__factory = None


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    collaborators = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    start_date = sqlalchemy.Column(sqlalchemy.DateTime)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    def __repr__(self):
        return f'<Job> {self.job}'


def global_init(db_name):
    global __factory
    if __factory:
        return
    engine = create_engine(f'sqlite:///{db_name}', echo=False)
    SqlAlchemyBase.metadata.create_all(engine)
    __factory = sessionmaker(bind=engine)


def create_session():
    global __factory
    return __factory() if __factory else None


db_name = input().strip()
global_init(db_name)
session = create_session()

if session:
    session.query(User).filter(User.address == 'module_1', User.age < 21).update(
        {User.address: 'module_3'}, synchronize_session='fetch'
    )
    session.commit()
