package main

import (
	"fmt"
)

func DoubleNumbers(done <-chan struct{}, in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for num := range in {
			select {
			case <-done:
				return
			default:
				out <- num * 2
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

	result := DoubleNumbers(done, nums)

	for num := range result {
		fmt.Printf("%d ", num)
	}
}
