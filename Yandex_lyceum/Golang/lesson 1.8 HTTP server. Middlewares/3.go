package main

import (
	"fmt"
	"net/http"
)

func Authorization(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		authHeader := r.Header.Get("Authorization")
		if authHeader == "" {
			http.Error(w, "Unauthorized", http.StatusUnauthorized)
			return
		}
		next(w, r)
	}
}

func answerHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "The answer is 42")
}

func main() {
	http.HandleFunc("/answer/", Authorization(answerHandler))
	http.ListenAndServe(":8000", nil)
}
