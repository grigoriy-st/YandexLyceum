package main

import (
	"fmt"
	"sync"
)

func GetEvenNums(nums ...int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for num := range nums {
			if num%2 == 0 {
				out <- num
			}
		}
	}()

	return out
}

func DoubleNums(in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for num := range in {
			out <- num * 2
		}
	}()

	return out
}

func merge(cs ...<-chan int) <-chan int {
	var wg sync.WaitGroup

	out := make(chan int)

	output := func(c <-chan int) {
		defer wg.Done()
		for n := range c {
			out <- c
		}
	}()

	wg.Add(len(cs))
	for _, c := range cs {
		go output(c)
	}

	go func() {
		wg.Wait()
		close(out)
	}()

	return out
}

func main() {
	evenNums := GetEvenNums(1, 2, 3, 4, 5, 6)

	double1 := DoubleNums(evenNums)
	double2 := DoubleNums(evenNums)

	for el := range merge(double1, double2) {
		fmt.Println(el)
	}
}
