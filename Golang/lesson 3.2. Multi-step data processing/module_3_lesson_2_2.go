package main

import (
	"fmt"
)

func ToString[T any](done <-chan struct{}, valueStream <-chan T) <-chan string {
	out := make(chan string)

	go func() {
		defer close(out)
		for val := range valueStream {
			select {
			case <-done:
				return
			default:
				out <- fmt.Sprint(val)
			}
		}
	}()
	return out
}

func main() {
	done := make(chan struct{})
	defer close(done)

	nums := make(chan int)
	go func() {
		for i := 1; i <= 5; i++ {
			nums <- i
		}
		close(nums)
	}()

	result := ToString(done, nums)

	for num := range result {
		fmt.Printf("%s ", num)
	}
}
