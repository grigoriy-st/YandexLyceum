import requests

BASE_URL = "http://127.0.0.1:8080"

def test_get_all_jobs():
    response = requests.get(f"{BASE_URL}/api/jobs")
    assert response.status_code == 200, "Ошибка: Не удалось получить все работы"
    print("Тест получения всех работ пройден.")

def test_get_job_by_id():
    job_id = 1
    response = requests.get(f"{BASE_URL}/api/job/{job_id}")
    assert response.status_code == 200, "Ошибка: Не удалось получить работу по ID"
    print("Тест получения работы по ID пройден.")

def test_get_job_by_invalid_id():
    invalid_id = 9999
    response = requests.get(f"{BASE_URL}/api/job/{invalid_id}")
    assert response.status_code == 404, "Ошибка: Ожидался 404 для несуществующего ID"
    print("Тест получения работы по несуществующему ID пройден.")

def test_get_job_by_string_id():
    string_id = "abc"
    response = requests.get(f"{BASE_URL}/api/job/{string_id}")
    assert response.status_code == 400, "Ошибка: Ожидался 400 для неверного ID"
    print("Тест получения работы по строковому ID пройден.")

if __name__ == "__main__":
    test_get_all_jobs()
    test_get_job_by_id()
    test_get_job_by_invalid_id()
    test_get_job_by_string_id()
