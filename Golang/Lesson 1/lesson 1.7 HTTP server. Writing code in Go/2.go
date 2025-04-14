package main

import (
	"fmt"
	"net/http"
	"time"
)

var curNum int
var f1, f2 = 0, 1

func FibonacciHandler(w http.ResponseWriter, r *http.Request) {
	if curNum < 2 {
		fmt.Fprintf(w, "%d", curNum)
		curNum++
		return
	}

	res := f1 + f2
	fmt.Fprintf(w, "%d", res)
	f1, f2 = f2, res

	curNum++
}

func StartServer(time.Duration) {
	http.HandleFunc("/", FibonacciHandler)

	if err := http.ListenAndServe(":8000", nil); err != nil {
		fmt.Println("Error starting server:", err)
	}
}

func main() {
	StartServer(time.Duration(10 * time.Second))
}
