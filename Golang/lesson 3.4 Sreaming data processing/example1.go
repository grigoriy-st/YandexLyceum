package main

import "fmt"

func EvenNumbersGen(numbers ...int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for _, num := range numbers {
			if num%2 == 0 {
				out <- num
			}
		}
	}()
	return out
}

func DoubleNumbers(in <-chan int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for num := range in {
			out <- num * 2
		}
	}()
	return out
}

func main() {
	evens := EvenNumbersGen(1, 2, 3, 4, 5, 6)
	out := DoubleNumbers(evens)

	for num := range out {
		fmt.Println(num)
	}
}
