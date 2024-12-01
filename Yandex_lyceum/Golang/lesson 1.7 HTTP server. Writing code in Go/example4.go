package main

import (
	"fmt"
	"net/http"
)

type apiHandler struct{}

func main() {
	mux := http.NewServeMux()

	mux.HandleFunc("/search", func(w http.ResponseWriter, r *http.Request) {
		query := r.URL.Query()

		searchQuery := query.Get("q")
		page := query.Get("page")

		if searchQuery == "" {
			http.Error(w, "missing 'q' parametr", http.StatusBadRequest)
			return
		}

		response := fmt.Sprintf("Search query: %s\nPage: %s", searchQuery, page)

		fmt.Fprintf(w, response)
	})

	if err := http.ListenAndServe(":8080", mux); err != nil {
		fmt.Println("Error starting server:", err)
	}
}
