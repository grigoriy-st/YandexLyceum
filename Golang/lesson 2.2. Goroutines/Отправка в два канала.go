package main

import "fmt"

func Send(ch1, ch2 chan int) {
	go func() {
		for i := 0; i < 3; i++ {
			ch1 <- i
		}
		close(ch1)
	}()

	go func() {
		for i := 0; i < 3; i++ {
			ch2 <- i
		}
		close(ch2)
	}()
}

func main() {
	ch1, ch2 := make(chan int), make(chan int)

	Send(ch1, ch2)

	for value := range ch1 {
		fmt.Println(value)
	}

	for value := range ch2 {
		fmt.Println(value)
	}
}
