package main

import (
	"fmt"
	"time"
)

func Receive(ch chan int) int {
	return <-ch
}

func main() {
	ch := make(chan int)
	go func() {
		time.Sleep(1 * time.Second)

		ch <- 3
		ch <- 5

	}()

	out := Receive(ch)
	fmt.Printf("%d", out)

}
