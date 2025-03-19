package main

import (
	"fmt"
	"net/http"
	"time"
)

var (
	curNum   int
	f1, f2   = 0, 1
	metrics  int
	reqCount int
)

func FibonacciHandler(w http.ResponseWriter, r *http.Request) {
	if curNum < 2 {
		fmt.Fprintf(w, "%d", curNum)
		curNum++
		reqCount++
		return
	}

	res := f1 + f2
	fmt.Fprintf(w, "%d", res)
	f1, f2 = f2, res

	curNum++
	reqCount++
}

func MetricsHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "rpc_duration_milliseconds_count %d", reqCount)
}

func StartServer(time.Duration) {
	http.HandleFunc("/", FibonacciHandler)
	http.HandleFunc("/metrics", MetricsHandler)

	if err := http.ListenAndServe(":8000", nil); err != nil {
		fmt.Println("Error starting server:", err)
	}
}

func main() {
	StartServer(time.Duration(10 * time.Second))
}
