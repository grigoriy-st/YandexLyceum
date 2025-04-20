import pytest
import requests

# URL вашего API
BASE_URL = 'http://localhost:8080/api/jobs'


def test_add_job_success():
    # Корректный запрос на добавление работы
    correct_request = {
        "id": 1234,
        "job_title": "Software Developer",
        "team_leader_id": 2,
        "work_size": 40,
        "collaborators": "3, 4",
        "author_id": 2,
        "is_finished": False
    }
    
    response = requests.post(BASE_URL, json=correct_request)
    assert response.status_code == 200
    print(response.json())
    assert response.json()['job']['status'] == 'JOB IS ADDED'

def test_delete_job_success():
    """ Удаление работы. """

    url = BASE_URL + '/delete/1234'
    print(url)
    response = requests.delete(url)
    assert response.status_code == 200
    assert response.json()['job']['status'] == 'deleted' 

def test_add_job_missing_field():
    # Некорректный запрос: отсутствует обязательное поле 'job_title'
    incorrect_request = {
        "id": 2,
        "team_leader_id": 2,
        "work_size": 40,
        "collaborators": "3, 4"
    }
    
    response = requests.post(BASE_URL, json=incorrect_request)
    assert response.status_code == 400
    assert 'error' in response.json()

def test_add_job_invalid_id():
    # Некорректный запрос: id не является числом
    incorrect_request = {
        "id": "abc",  # Некорректный id
        "job_title": "Software Developer",
        "team_leader_id": 2,
        "work_size": 40,
        "collaborators": "3, 4"
    }
    
    response = requests.post(BASE_URL, json=incorrect_request)
    assert response.status_code == 400


def test_add_job_duplicate_id():
    # Сначала добавим работу с id = 3
    correct_request = {
        "id": 3,
        "job_title": "Data Scientist",
        "team_leader_id": 2,
        "work_size": 40,
        "collaborators": "3, 4"
    }
    requests.post(BASE_URL, json=correct_request)

    # Теперь попробуем добавить работу с тем же id
    duplicate_request = {
        "id": 3,
        "job_title": "Data Analyst",
        "team_leader_id": 2,
        "work_size": 40,
        "collaborators": "3, 4"
    }
    
    response = requests.post(BASE_URL, json=duplicate_request)
    assert response.status_code == 400
    assert 'error' in response.json()

def test_get_all_jobs():
    # Запрос на получение всех работ
    response = requests.get(BASE_URL)
    assert response.status_code == 200
    assert 'jobs' in response.json()