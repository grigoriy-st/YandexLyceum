package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"unicode"
)

type Response struct {
	Greetings string `json:"greetings,omitempty"`
	Name      string `json:"name,omitempty"`
}

type RPCResponse struct {
	Status string   `json:"status"`
	Result Response `json:"result"`
}

func Sanitize(next http.HandlerFunc) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		query := r.URL.Query()
		searchQuery := query.Get("name")

		allLetters := true
		for _, r := range searchQuery {
			if !unicode.IsLetter(r) {
				allLetters = false
				break
			}
		}

		if !allLetters {
			w.Header().Set("Content-Type", "application/json")
			response := RPCResponse{
				Status: "error",
				Result: Response{},
			}
			w.WriteHeader(http.StatusOK)
			json.NewEncoder(w).Encode(response)
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
			r.URL.RawQuery = query.Encode()
		}
		next.ServeHTTP(w, r)
	}
}

func HelloHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	searchQuery := query.Get("name")

	response := Response{
		Greetings: "hello",
		Name:      searchQuery,
	}

	w.Header().Set("Content-Type", "application/json")
	rpcResponse := RPCResponse{
		Status: "ok",
		Result: response,
	}
	w.WriteHeader(http.StatusOK)
	json.NewEncoder(w).Encode(rpcResponse)
}

func RPC(next http.HandlerFunc) http.HandlerFunc {
	return next
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", RPC(SetDefaultName(Sanitize(HelloHandler))))

	if err := http.ListenAndServe(":8000", mux); err != nil {
		fmt.Println("Error starting server:", err)
	}
}
