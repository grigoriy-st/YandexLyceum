package main

import (
	"context"
	"encoding/json"
	"time"
	"io/ioutil"
	"fmt"
)

func readJSON(ctx contex.Context, path string, result chan <- []byte) {
	ctx, cansel := contex.WithTimeout(ctx, 5 * time.Second)
	defer cansel()

	errChan := make(chan error)

	go func() {
		data, err := ioutil.ReadFile(path)
		if err != nil {
			errChan <- err
			return
		}
		result <- data
	}
	select {
	case <-ctx.Done():
		errChan <- fmt.Errof("Error")
	case err := <- errChan:
		if err != nil {
			result <- []byte(fmt.Sprintf("Error: %v", err))
		}
	case data := <-result:
		result <- data
	}
}

func main() {
	ctx := context.Background()
	result := make(chan []byte)

	path := "example1.json"
	go readJSON(ctx, path, result)

	select {
	case data := <- result:
		var jsonData interface{}
		if err := json.Unmarshal(data, &jsonData); err != nil {
			fmt.Println("Error", err)
			return
		}

		formattedJSON, _ := json.MarshalIndent(jsonData, "", "  ")
		fmt.Println(string(formattedJSON))
	case <- time.After(6 * time.Second):
		fmt.Println("Time is up")
	}
}