package main

import (
    "fmt"
    "io/ioutil"
    "net/http"
    "time"
)

func StartServer(maxTimeout time.Duration) {
    http.HandleFunc("/readSource", func(w http.ResponseWriter, r *http.Request) {
        client := &http.Client{
            Timeout: maxTimeout,
        }

        resp, err := client.Get("http://localhost:8081/provideData")
        if err != nil {
            http.Error(w, "Service Unavailable", http.StatusServiceUnavailable)
            return
        }
        defer resp.Body.Close()

        body, err := ioutil.ReadAll(resp.Body)
        if err != nil {
            http.Error(w, "Error reading response", http.StatusInternalServerError)
            return
        }

        w.WriteHeader(resp.StatusCode)
        w.Write(body)
    })

    fmt.Println("Starting server on http://localhost:8080")
    if err := http.ListenAndServe(":8080", nil); err != nil {
        fmt.Printf("Error starting server: %v\n", err)
    }
}

func main() {
    maxTimeout := 2 * time.Second // Установите желаемый таймаут
    StartServer(maxTimeout)
}