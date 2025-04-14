package main

import (
	"fmt"
	"time"
)

func Tee[T any](done <-chan struct{},
	in <-chan T) (<-chan T, <-chan T) {
	chan1 := make(chan T)
	chan2 := make(chan T)

	go func() {
		defer close(chan1)
		defer close(chan2)

		for {
			select {
			case <-done:
				return
			case val, ok := <-in:
				if !ok {
					return
				}
				chan1 <- val
				chan2 <- val
			}
		}
	}()
	return chan1, chan2
}

func main() {
	done := make(chan struct{})
	in := make(chan int)

	chan1, chan2 := Tee(done, in)

	go func() {
		for i := 0; i < 5; i++ {
			in <- i
			time.Sleep(100 * time.Millisecond)
		}
		close(in)
	}()

	go func() {
		for val := range chan1 {
			fmt.Println("Chan1:", val)
		}
	}()

	go func() {
		for val := range chan2 {
			fmt.Println("Chan2:", val)
		}
	}()

	time.Sleep(1 * time.Second)
	close(done)
}
