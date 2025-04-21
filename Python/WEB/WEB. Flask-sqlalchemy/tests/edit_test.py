import pytest
import requests

BASE_URL = 'http://localhost:8080/api/jobs/edit'


def test_correct_editing_1():
    correct_request = {
        "id": 10,
        "team_leader": 2,
        "work_size": 40,
        "collaborators": "3, 4",
    }

    response = requests.put(BASE_URL, json=correct_request)
    assert response.status_code == 200
    assert response.json()['job'] == 'updated successfully'


def test_correct_editing_2():
    correct_request = {
        "id": 10,
        "team_leader": 2,
        "work_size": 55,
        "collaborators": "11, 12",
    }

    response = requests.put(BASE_URL, json=correct_request)
    assert response.status_code == 200
    assert response.json()['job'] == 'updated successfully'


def test_not_existing_id():
    """ Проверка на несуществующую работу. """
    correct_request = {
        "id": 9999,
        "team_leader": 2,
    }

    response = requests.put(BASE_URL, json=correct_request)
    assert response.status_code == 400
    assert response.json()['error'] == 'job is not found'


def test_incorrect_field():
    """ Проверка на неверное поле для объекта Job. """
    incorrect_request = {
        "id": 10,
        "new_field": 2,
    }

    response = requests.put(BASE_URL, json=incorrect_request)
    assert response.status_code == 400
    assert response.json()['error'] == 'field new_field not available'

def test_empty_query():
    """ Запрос с пустыми полями. """

    response = requests.put(BASE_URL, json={})
    assert response.status_code == 400
    assert response.json()['error']== 'Empty sending fields'

def test_get_all_jobs():
    """ Получение всех работ. """
       
    response = requests.get('http://localhost:8080/api/jobs')

    assert response.status_code == 200
    assert response.json()['status']== 'all works have been recieved' 