import unittest
import json
from main import app
from data import db_session
from models.users import User
from flask import abort

def abort_if_user_not_found(users_id):
    try:
        session = db_session.create_session()
        users = session.query(User).filter(User.id == users_id).first()
        if not users:
            abort(404, message=f"user {users_id} not found")
    finally:
        session.close()

class UsersResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.session = db_session.create_session()
        self.created_users = []  # Список для хранения ID созданных пользователей

        # Создаем тестового пользователя
        user = User(
            id=1010,
            name='Test User',
            position='Teacher',
            email='test123@example.com'
        )
        user.set_password('password123')
        self.session.add(user)
        self.session.commit()
        self.created_users.append(user.id)

    def tearDown(self):
        """ Удаление только созданных пользователей. """
        for user_id in self.created_users:
            user = self.session.query(User).filter(User.id == user_id).first()
            if user:
                self.session.delete(user)
        self.session.commit()
        self.session.close()

    def test_get_user(self):
        """ Получение информации по пользователю. """
        # abort_if_user_not_found(1010)
        response = self.app.get('/api/v2/users/1010')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test User', str(response.data))

    def test_get_nonexistent_user(self):
        """ Получение несуществующего пользователя. """
        response = self.app.get('/api/v2/users/999')
        self.assertEqual(response.status_code, 404)

    def test_post_user(self):
        """ Добавление пользователя."""

        new_user_data = {
            'id': '1002',
            'name': 'New User',
            'position': 'Swimmer',
            'email': 'new123@example.com',
            'hashed_password': 'newpassword',
            'created_date': '2025-03-26 02:17:37'
        }
        response = self.app.post('/api/v2/users', data=json.dumps(new_user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())
        self.created_users.append(1002)

    def test_post_user_without_password(self):
        """ Добавление пользователя без пароля. """
        new_user_data = {
            'id': 1003,
            'name': 'Another User',
            'position': 'Engineer',
            'created_date': '2025-03-26 02:17:37'
        }
        response = self.app.post('/api/v2/users', data=json.dumps(new_user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_user(self):
        """ Удаление пользователя. """
        response = self.app.delete('/api/v2/users/1002')
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', str(response.data))

    def test_delete_nonexistent_user(self):
        """ Удаление несущствующего пользователя. """
        response = self.app.delete('/api/v2/users/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()