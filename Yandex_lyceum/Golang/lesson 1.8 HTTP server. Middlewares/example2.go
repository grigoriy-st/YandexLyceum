package main

import (
	"fmt"
	"log"
	"net/http"
)

func PanicMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		defer func() {
			if err := recover(); err != nil {
				log.Printf("Panic: %v", err)
				http.Error(w, http.StatusText(http.StatusInternalServerError), http.StatusInternalServerError)
			}
		}()
		next.ServeHTTP(w, r)
	})
}

func HomeHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("The HomeHandler is worked"))
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", HomeHandler)

	handler := PanicMiddleware(mux)
	if err := http.ListenAndServe(":8000", handler); err != nil {
		fmt.Println("Error starting server:", mux)
	}
}
