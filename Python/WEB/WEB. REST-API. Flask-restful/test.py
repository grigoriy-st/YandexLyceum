# from data import users_resource
from data.users_resource import delete, post, get

print(get('http://localhost:5000/api/users/1').json())
print(get('http://localhost:5000/api/users').json())

print(get('http://localhost:5000/api/users/999').json())
print(get('http://localhost:5000/api/users/q').json())
print(post('http://localhost:5000/api/users', json={}).json())

print(post('http://localhost:5000/api/users',
           json={'name': 'Заголовок'}).json())

print(post('http://localhost:5000/api/users',
           json={'name': 'Марсианин 1',
                 'about': 'Текст',
                 'email': "first@mail.com",
                 'hashed_password': "123"
                 }).json())

print(delete('http://localhost:5000/api/users/999').json())
# новости с id = 999 нет в базе

print(delete('http://localhost:5000/api/users/1').json())
