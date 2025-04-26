import unittest
import json
from main import app
from data import db_session
from models.jobs import Jobs
from flask import abort


def abort_if_job_not_found(jobs_id):
    try:
        session = db_session.create_session()
        job = session.query(Jobs).filter(Jobs.id == int(jobs_id)).first()
        if not job:
            abort(404, message=f"job {jobs_id} not found")
    finally:
        session.close()


class JobsResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.session = db_session.create_session()

        # Список для хранения ID созданных работ
        self.created_jobs = []

        # Создаем тестовую работу
        job = Jobs(
            id=1010,
            job_title='Test Job',
            author='3',
            team_leader='15',
            work_size='50',
        )

        self.session.add(job)
        self.session.commit()
        self.created_jobs.append(job.id)

    def tearDown(self):
        """ Удаление только созданных работ. """
        for jobs_id in self.created_jobs:
            job = self.session.query(Jobs).filter(Jobs.id == int(jobs_id)).first()
            if job:
                self.session.delete(job)
        self.session.commit()
        self.session.close()

    def test_get_job(self):
        """ Получение информации по работе. """
        response = self.app.get('/api/v2/jobs/1010')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Job', str(response.data))

    def test_get_nonexistent_job(self):
        """ Получение несуществующей работы. """
        response = self.app.get('/api/v2/jobs/999')
        self.assertEqual(response.status_code, 404)

    def test_post_job(self):
        """ Добавление работы. """

        new_job_data = {
            'id': 1002,
            'job_title': 'Test Job',
            'author': 10,
            'team_leader': 16,
            'work_size': 25,
            'collaborators': '1, 2, 3',
            'hazard_category': 3,
        }
        response = self.app.post('/api/v2/jobs',
                                 data=json.dumps(new_job_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.get_json())
        self.created_jobs.append(new_job_data['id'])

    def test_post_job_without_worksize(self):
        """ Добавление работы без обязательного поля work_size. """
        new_job_data = {
            'id': 1010,
            'job_title': 'Test Job 3',
            'author': 10,
            'team_leader': 16,
        }
        response = self.app.post('/api/v2/jobs',
                                 data=json.dumps(new_job_data),
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_delete_job(self):
        """ Удаление работы. """
        
        new_job_data = {
            'id': 1006,
            'job_title': 'Test Job',
            'author': 10,
            'team_leader': 16,
            'work_size': 25,
            'collaborators': '1, 2, 3',
            'hazard_category': 3,
        }
        response = self.app.post('/api/v2/jobs',
                                 data=json.dumps(new_job_data),
                                 content_type='application/json')
        
        response = self.app.delete('/api/v2/jobs/1006')
        self.assertEqual(response.status_code, 200)
        self.assertIn('OK', str(response.data))
        self.created_jobs.append(new_job_data['id'])

    def test_delete_nonexistent_job(self):
        """ Удаление несущствующей работы. """
        response = self.app.delete('/api/v2/jobs/999')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
