package main

import (
	"context"
	"fmt"
	"time"
)

func main() {
	ctx, cansel := context.WithTimeout(context.Background(), 4*time.Second)
	defer cansel()

	chan_c := make(chan string)
	// chan_c <- "String in buf"

	go func() {
		time.Sleep(3 * time.Second)
		chan_c <- "Success"
	}()

	select {
	case result := <-chan_c:
		fmt.Println("It worked", result)
	case <-ctx.Done():
		fmt.Println("Time's up")
	}
}
