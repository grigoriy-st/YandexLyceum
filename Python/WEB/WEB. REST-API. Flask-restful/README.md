# Данные

## Структура папок и файлов проекта

```
alembic     // Файлы alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── alembic.ini
├── api     // API Rest
│   ├── jobs_api.py
│   └── users_api.py
├── data    // Работа с БД
│   ├── __all_models.py
│   └── db_session.py
├── db      // БД
│   └── blogs.sqlite
├── forms   // Формы
│   ├── DepartmentForm.py
│   ├── LoginForm.py
│   ├── NewsForm.py
│   └── user.py
├── handlers // Обработчики
│   ├── auth.py
│   ├── work_with_departments.py
│   ├── work_with_jobs.py
│   ├── work_with_news.py
│   └── work_with_users.py
├── models
│   ├── data_parser.py
│   ├── departments.py
│   ├── hazard_category.py
│   ├── jobs.py
│   ├── news.py
│   └── users.py
├── myenv       // Для среды с linux
├── parsers     // Парсеры 
│   ├── job_parser.py
│   └── users_parser.py
├── sources     // Ресурсы Rest Full API
│   ├── jobs_resource.py
│   ├── news_resources.py
│   └── users_resource.py
├── static      // Статические файлы
│   ├── css
│   └── imgs
├── templates   // HHTML-шаблоны
│   ├── add_department.html
│   ├── base.html
│   ├── dep_for_editing.html
│   ├── index.html
│   ├── job_for_editing.html
│   ├── jobs.html
│   ├── list_of_departments.html
│   ├── login.html
│   ├── new_job.html
│   ├── news.html
│   ├── personal_page.html
│   ├── register.html
│   └── user_list.html
└── tests
    ├── test_Jobs_API1.py       // Rest API тесты на `pytest`
    ├── test_Jobs_API2.py
    ├── test_Jobs_API3.py
    ├── test_Jobs_Resource_RESTFULL.py      // Rest Full API тесты на `unittest`
    └── test_Users_Resource_RESTFULL.py

main.py
```

## Как тестировать

### Pytest

```bash
pytest test/test_Jobs_API1.py
```

```bash
pytest test/test_Jobs_API1.py
```

```bash
pytest test/test_Jobs_API1.py
```

### Unittest

```bash
python -m unittest test/test_Jobs_Resource_RESTFULL.py
```

```bash
python -m unittest test/test_Users_Resource_RESTFULL.py
```

## Ручные тесты Rest Full API. Requests

### News

GET-запрос на получение новостей

```bash
curl -X GET http://localhost:8080/api/v2/news
```

POST-запрос на добавление новости

```bash
curl -X POST http://localhost:8080/api/v2/news \
-H "Content-Type: application/json" \
-d '{
    "title": "News title",
    "content": "News content",
    "is_private": true,
    "is_published": true,
    "user_id": 1
}'
```

### Users

Получение информации по пользователю

```bash
curl -X GET http://localhost:8080/api/v2/users/1 \
-H "Content-Type: application/json"
```

Добавление нового пользователя

```bash
curl -X POST http://localhost:8080/api/v2/users \
-H "Content-Type: application/json" \
-d '{
    "id": 105,
    "name": "User_name1",
    "about": "Info about User_name1",
    "email": "user@example.com",
    "created_date": "2023-10-01T12:00:00",
    "hashed_password": "password123"
}'
```
### Jobs

#### 1. Получение существующей работы (`test_get_job`)
```bash
curl -X GET http://localhost:8080/api/v2/jobs/1010
```

#### 2. Получение несуществующей работы (`test_get_nonexistent_job`)
```bash
curl -X GET http://localhost:8080/api/v2/jobs/999
```
Ожидаемый результат: 404 Not Found

#### 3. Добавление новой работы (`test_post_job`)
```bash
curl -X POST http://localhost:8080/api/v2/jobs \
-H "Content-Type: application/json" \
-d '{
    "id": 1002,
    "job_title": "Test Job",
    "author": 10,
    "team_leader": 16,
    "work_size": 25,
    "collaborators": "1, 2, 3",
    "hazard_category": 3
}'
```

#### 4. Попытка добавить работу без work_size (`test_post_job_without_worksize`)

```bash
curl -X POST http://localhost:8080/api/v2/jobs \
-H "Content-Type: application/json" \
-d '{
    "id": 1010,
    "job_title": "Test Job 3",
    "author": 10,
    "team_leader": 16
}'
```

#### 5. Удаление существующей работы (`test_delete_job`)

Создание работы:
```bash
curl -X POST http://localhost:8080/api/v2/jobs \
-H "Content-Type: application/json" \
-d '{
    "id": 1006,
    "job_title": "Test Job",
    "author": 10,
    "team_leader": 16,
    "work_size": 25,
    "collaborators": "1, 2, 3",
    "hazard_category": 3
}'
```

Удалление созданной работы:
```bash
curl -X DELETE http://localhost:8080/api/v2/jobs/1006
```

### 6. Попытка удалить несуществующую работу (`test_delete_nonexistent_job`)

```bash
curl -X DELETE http://localhost:8080/api/v2/jobs/999
```
