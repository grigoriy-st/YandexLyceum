package main

import "fmt"

func Send(ch chan int, num int) {
	ch <- num
}

func main() {
	ch := make(chan int)

	go Send(ch, 3)

	out := <-ch
	fmt.Printf("%d", out)
}
