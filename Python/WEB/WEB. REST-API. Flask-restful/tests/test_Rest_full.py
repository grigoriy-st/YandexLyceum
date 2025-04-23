import unittest
import json
from main import app
from data import db_session
from models.users import User

class UsersResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.session = db_session.create_session()
        self.created_users = []  # Список для хранения ID созданных пользователей

        # Создаем тестового пользователя
        user = User(
            id=1,
            name='Test User',
            about='This is a test user.',
            email='test@example.com'
        )
        user.set_password('password123')
        self.session.add(user)
        self.session.commit()
        self.created_users.append(user.id)  # Сохраняем ID созданного пользователя

    def tearDown(self):
        # Удаляем только созданных пользователей
        for user_id in self.created_users:
            user = self.session.query(User).get(user_id)
            if user:
                self.session.delete(user)
        self.session.commit()
        self.session.close()

    def test_get_user(self):
        response = self.app.get('/api/v2/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test User', str(response.data))

    def test_get_nonexistent_user(self):
        response = self.app.get('/api/v2/users/999')
        self.assertEqual(response.status_code, 404)

    def test_post_user(self):
        new_user_data = {
            'id': 2,
            'name': 'New User',
            'about': 'This is a new user.',
            'email': 'new@example.com',
            'hashed_password': 'newpassword',
            'created_date': '2023-01-02'
        }
        response = self.app.post('/api/v2/users', data=json.dumps(new_user_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('id', response.get_json())
        self.created_users.append(response.get_json()['id'])  # Сохраняем ID нового пользователя

    def test_post_user_without_email(self):
        new_user_data = {
            'id': 3,
            'name': 'Another User',
            'about': 'This user has no email.',
            'hashed_password': 'anotherpassword',
            'created_date': '2023-01-03'
        }
        response = self.app.post('/api/v2/users', data=json.dumps(new_user_data), content_type='application/json')
        self.assertEqual(response.status_code, 400)  # Предполагается, что вы обрабатываете ошибки валидации

    def test_delete_user(self):
        response = self.app.delete('/api/v2/users/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', str(response.data))

    def test_delete_nonexistent_user(self):
        response = self.app.delete('/api/v2/users/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()