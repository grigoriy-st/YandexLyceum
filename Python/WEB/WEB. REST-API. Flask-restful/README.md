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
