import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from users import User
from jobs import Jobs
from users import SqlAlchemyBase
from sqlalchemy import DateTime

engine = create_engine("sqlite:///mars_explorer.sqlite", echo=True)
SqlAlchemyBase.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

captain = User(
    surname='Scott',
    name='Ridley',
    age=21,
    position='captain',
    speciality='research engineer',
    address='module_1',
    email='scott_chief@mars.org'
)

colonists = [
    User(
        surname='Johnson',
        name='Emily',
        age=30,
        position='medic',
        speciality='biomedical scientist',
        address='module_2',
        email='johnson_medic@mars.org'
    ),
    User(
        surname='Smith',
        name='Daniel',
        age=28,
        position='engineer',
        speciality='mechanical engineer',
        address='module_3',
        email='smith_engineer@mars.org'
    ),
    User(
        surname='Williams',
        name='Sophia',
        age=26,
        position='botanist',
        speciality='scientist',
        address='module_4',
        email='williams_botanist@mars.org'
    ),
]

session.add(captain)
session.add_all(colonists)
session.commit()
session.close()

