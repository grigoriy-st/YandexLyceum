package main

import (
	"fmt"
	"net/http"
)

func helloHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "This is example use http.Handler")
}

func showSimplePage(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "<h2>This is simple page</h2>")
}

func main() {
	http.HandleFunc("/", helloHandler)
	http.HandleFunc("/simple_page", showSimplePage)

	http.ListenAndServe(":8080", nil)
}
