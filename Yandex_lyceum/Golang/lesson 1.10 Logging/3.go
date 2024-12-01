package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
)

type Response struct {
	Name string `json:"name""`
}

func HelloHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()
	name := query.Get("name")

	response := Response{Name: name}
	tempData, err := json.Marshal(response)
	if err != nil {
		log.Printf("Error in JSON ops: %v", err)
		return
	}

	log.Printf("%s", tempData)

	w.Header().Set("Content-Type", "application'json")
	w.WriteHeader(http.StatusOK)

	json.NewEncoder(w).Encode(response)
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/hello", HelloHandler)

	if err := http.ListenAndServe(":8000", mux); err != nil {
		fmt.Println("Error starting server", err)
	}
}
