# Данные по задачам

## Рабочие запросы

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

Получение всех пользователей

```bash
curl -X GET http://localhost:8080/api/v2/users \
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
