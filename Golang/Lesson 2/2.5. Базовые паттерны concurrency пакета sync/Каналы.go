package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan struct{})

	go func() {
		fmt.Println("Start computing")

		time.Sleep(3 * time.Second)
		fmt.Println("End computing")

		close(ch)
	}()

	<-ch
	fmt.Println("Exit program")
}
