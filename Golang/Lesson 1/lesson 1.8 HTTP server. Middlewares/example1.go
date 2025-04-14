package main

import (
	"fmt"
	"log"
	"net/http"
	"time"
)

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()

		log.Printf("Query: %s %s", r.Method, r.URL.Path)
		next.ServeHTTP(w, r)
		duration := time.Since(start)
		log.Printf("Request execution time: %s", duration)
	})
}

func helloHandler(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Hello, world!"))
}

func main() {
	mux := http.NewServeMux()
	hello := http.HandlerFunc(helloHandler)

	mux.Handle("/", loggingMiddleware(hello))
	if err := http.ListenAndServe(":8000", mux); err != nil {
		fmt.Println("Error starting server:", err)
	}

}
