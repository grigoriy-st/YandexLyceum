package main

import (
	"fmt"
	"net/http"
	"unicode"
)

func StrangerHandler(w http.ResponseWriter, r *http.Request) {
	query := r.URL.Query()

	searchQuery := query.Get("name")
	if searchQuery == "" {
		fmt.Fprintf(w, "hello stranger")
		return
	}

	queryRune := []rune(searchQuery)

	all_letters := true
	for _, r := range queryRune {
		if !unicode.IsLetter(r) {
			all_letters = false
			break
		}
	}
	if all_letters == false {
		fmt.Fprintf(w, "hello dirty hacker")
	} else {
		fmt.Fprintf(w, "hello %s", searchQuery)
	}
}

func main() {
	mux := http.NewServeMux()
	mux.HandleFunc("/", StrangerHandler)

	if err := http.ListenAndServe(":8080", mux); err != nil {
		fmt.Println("Error starting serrver:", err)
	}

}
