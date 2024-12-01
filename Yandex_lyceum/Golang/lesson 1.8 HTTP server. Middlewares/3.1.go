package main

import (
	"encoding/base64"
	"fmt"
	"net/http"
	"strings"
)

const (
	// Укажите ваши учетные данные
	validUsername = "userid"
	validPassword = "password"
)

// Authorization - middleware-функция для проверки заголовка Authorization
func Authorization(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		authHeader := r.Header.Get("Authorization")
		if authHeader == "" {
			// Если заголовок отсутствует, возвращаем 401 Unauthorized
			w.Header().Set("WWW-Authenticate", "Basic realm=\"Restricted\"")
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}

		// Проверяем, что заголовок начинается с "Basic "
		if !strings.HasPrefix(authHeader, "Basic ") {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}

		// Извлекаем и декодируем учетные данные
		payload := authHeader[len("Basic "):]
		decoded, err := base64.StdEncoding.DecodeString(payload)
		if err != nil {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}

		// Разделяем имя пользователя и пароль
		credentials := strings.SplitN(string(decoded), ":", 2)
		if len(credentials) != 2 || credentials[0] != validUsername || credentials[1] != validPassword {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}

		// Если авторизация успешна, передаем управление следующему обработчику
		next(w, r)
	}
}

// answerHandler - обработчик для маршрута /answer/
func answerHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "The answer is 42")
}

func main() {
	http.HandleFunc("/answer/", Authorization(answerHandler))

	// Запускаем сервер на порту 8080
	fmt.Println("Сервер запущен на http://localhost:8080")
	if err := http.ListenAndServe(":8080", nil); err != nil {
		fmt.Println("Ошибка при запуске сервера:", err)
	}
}
