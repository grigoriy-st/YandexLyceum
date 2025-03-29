import datetime
import sqlalchemy
from sqlalchemy import create_engine, ForeignKey, func
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

SqlAlchemyBase = declarative_base()


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    last_name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    jobs = relationship("Jobs", back_populates="team_leader_user")
    departments = relationship("Department", secondary="department_members", back_populates="members")


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    team_leader = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('users.id'), nullable=False)
    work_size = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    team_leader_user = relationship("User ", back_populates="jobs")


class Department(SqlAlchemyBase):
    __tablename__ = 'departments'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    chief = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('users.id'), nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    chief_user = relationship("User ", back_populates="departments")
    members = relationship("User ", secondary="department_members", back_populates="departments")


class DepartmentMembers(SqlAlchemyBase):
    __tablename__ = 'department_members'

    department_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('departments.id'), primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('users.id'), primary_key=True)


def global_init(db_name):
    engine = create_engine(f'sqlite:///{db_name}')
    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    engine = create_engine(f'sqlite:///mars_explorer_2.sqlite')
    Session = sessionmaker(bind=engine)
    return Session()


db_name = input()
global_init(db_name)

session = create_session()

department_id = 1

results = session.query(
    User.first_name, User.last_name
).join(Jobs, User.id == Jobs.team_leader).filter(
    Jobs.work_size > 25,
    User.id.in_(
        session.query(Department.members).filter(Department.id == department_id)
    )
).all()

for first_name, last_name in results:
    print(f"{last_name} {first_name}")

session.close()
