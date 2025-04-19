import pytest
import requests
import json

BASE_URL = 'http://localhost:8080'

# Фикстуры
@pytest.fixture
def sample_job_data():
    """Фикстура с корректными данными работы"""
    return {
        "id": 1001,
        "job_title": "Тестовая работа",
        "team_leader_id": 1,
        "work_size": 10,
        "collaborators": "2,3",
        "author_id": 1,
        "is_finished": False,
        "hazard_category": 2
    }

@pytest.fixture
def cleanup_jobs():
    """Фикстура для очистки тестовых данных"""
    yield  # Здесь можно добавить код предварительной очистки
    # Удаляем тестовые работы после тестов
    test_job_ids = [1001, 1002, 1003, 1004]
    for job_id in test_job_ids:
        requests.delete(f"{BASE_URL}/api/jobs/{job_id}")

# Вспомогательные функции
def get_all_jobs():
    response = requests.get(f"{BASE_URL}/api/jobs")
    response.raise_for_status()
    return response.json().get('jobs', [])

def find_job_by_id(job_id):
    jobs = get_all_jobs()
    return next((job for job in jobs if job.get('id') == job_id), None)

# Тесты
class TestJobCreation:
    """Тесты для создания работ"""

    def test_valid_job_creation(self, sample_job_data, cleanup_jobs):
        """Тест корректного создания работы"""
        response = requests.post(f"{BASE_URL}/api/jobs", json=sample_job_data)

        assert response.status_code == 201
        print('Вот ответ', response.json())
        assert response.json().get('success') == 'Job added'

        # Проверяем что работа появилась в списке
        job = find_job_by_id(sample_job_data['id'])
        assert job is not None
        assert job['job_title'] == sample_job_data['job_title']

    @pytest.mark.parametrize("test_case", [
        {
            "name": "missing_field",
            "data": {
                "id": 1002,
                "job_title": "Неполная работа",
                "team_leader_id": 1,
                "collaborators": "2,3"
            },
            "expected_status": 400,
            "error_keyword": "Missing required fields"
        },
        {
            "name": "invalid_type",
            "data": {
                "id": 1003,
                "job_title": "Работа с ошибкой",
                "team_leader_id": 1,
                "work_size": "десять",
                "collaborators": "2,3"
            },
            "expected_status": 400,
            "error_keyword": "Invalid type"
        },
        {
            "name": "duplicate_id",
            "data": {
                "id": 1001,  # Должен совпадать с sample_job_data
                "job_title": "Дублирующая работа",
                "team_leader_id": 1,
                "work_size": 5,
                "collaborators": "4,5"
            },
            "expected_status": 400,
            "error_keyword": "already exists"
        },
        {
            "name": "invalid_hazard",
            "data": {
                "id": 1004,
                "job_title": "Работа с неверной категорией",
                "team_leader_id": 1,
                "work_size": 8,
                "collaborators": "2,3",
                "hazard_category": 99
            },
            "expected_status": 400,
            "error_keyword": "Invalid hazard category"
        }
    ])
    def test_invalid_requests(self, test_case, sample_job_data, cleanup_jobs):
        """Параметризованный тест некорректных запросов"""
        # Сначала создаем валидную работу для теста дубликата
        if test_case['name'] == 'duplicate_id':
            requests.post(f"{BASE_URL}/api/jobs", json=sample_job_data)

        response = requests.post(f"{BASE_URL}/api/jobs", json=test_case['data'])

        assert response.status_code == test_case['expected_status']
        assert test_case['error_keyword'].lower() in response.json().get('error', '').lower()

class TestJobRetrieval:
    """Тесты для получения работ"""

    def test_get_all_jobs(self, sample_job_data, cleanup_jobs):
        """Тест получения списка работ"""
        # Сначала создаем тестовую работу
        requests.post(f"{BASE_URL}/api/jobs", json=sample_job_data)

        response = requests.get(f"{BASE_URL}/api/jobs")

        assert response.status_code == 200
        jobs = response.json().get('jobs', [])
        assert isinstance(jobs, list)
        assert any(job['id'] == sample_job_data['id'] for job in jobs)

    def test_get_single_job(self, sample_job_data, cleanup_jobs):
        """Тест получения конкретной работы"""
        # Сначала создаем тестовую работу
        requests.post(f"{BASE_URL}/api/jobs", json=sample_job_data)

        response = requests.get(f"{BASE_URL}/api/jobs/{sample_job_data['id']}")

        assert response.status_code == 200
        job = response.json().get('job')
        assert job['id'] == sample_job_data['id']
        assert job['job_title'] == sample_job_data['job_title']
