package main

import (
	"fmt"
	"net/http"
	"time"
)

var (
	f1, f2   = 0, 1
	reqCount = 0
	numCount = 0
)

func FibbonacciHandler(w http.ResponseWriter, r *http.Request) {
	if numCount < 2 {
		fmt.Fprintf(w, "%d", numCount)
		numCount++
		return
	}

	res := f1 + f2
	fmt.Fprintf(w, "%d", res)
	f1, f2 = f2, res

	numCount++
	reqCount++
}

func MetricHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "rpc_duration_milliseconds_count %d", reqCount)
}

func StartServer(time.Duration) {
	http.HandleFunc("/", FibbonacciHandler)
	http.HandleFunc("/metric", MetricHandler)

	if err := http.ListenAndServe(":8000", nil); err != nil {
		fmt.Println("Error starting server:", err)
	}
}

func main() {
	StartServer(10 * time.Second)
}
