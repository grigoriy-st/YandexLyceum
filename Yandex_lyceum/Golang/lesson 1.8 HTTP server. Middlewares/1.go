package main

import (
	"fmt"
	"net/http"
	"unicode"
)

func Sanitize(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		query := r.URL.Query()
		searchQuery := query.Get("name")

		all_letters := true
		for _, r := range searchQuery {
			if !unicode.IsLetter(r) {
				all_letters = false
				break
			}
		}

		if all_letters == false {
			fmt.Fprintf(w, "Hello, dirty hacker!")
			return
		}
		next.ServeHTTP(w, r)
	}
}

func SetDefaultName(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		query := r.URL.Query()
		searchQuery := query.Get("name")

		if searchQuery == "" {
			query.Set("name", "stranger")

			r = r.WithContext(r.Context())
			r.URL.RawQuery = query.Encode()
		}
		next.ServeHTTP(w, r)
	}
}

func HelloHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	searchQuery := query.Get("name")

	fmt.Fprintf(w, "Hello, %s!", searchQuery)
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", SetDefaultName(Sanitize(HelloHandler)))

	if err := http.ListenAndServe(":8000", mux); err != nil {
		fmt.Println("Error starting serrver:", err)
	}

}
