package main

import (
	"fmt"
	"time"
)

func main() {
	chan_c := make(chan string)

	go func() {

		time.Sleep(1 * time.Second)
		chan_c <- "This string in buf"
	}()

	timeout := time.AfterFunc(2*time.Second, func() {
		chan_c <- "Time`s up"
	})
	result := <-chan_c

	fmt.Println(result)
	timeout.Stop()
}
