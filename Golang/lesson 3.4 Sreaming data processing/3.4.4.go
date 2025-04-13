package main

import "fmt"

func MultiplyPipeline(inputNums ...[]int) int {
	numsChan := NumbersGen(inputNums...)
	filteredChan := Filter(numsChan)

	return Multiply(filteredChan)
}

func NumbersGen(nums ...[]int) <-chan int {
	out := make(chan int)

	go func() {
		defer close(out)

		for _, slice := range nums {
			for _, el := range slice {
				out <- el
			}
		}
	}()
	return out
}

func Filter(in <-chan int) <-chan int {
	out := make(chan int)

	go func() {
		defer close(out)

		for num := range in {
			if num > 0 {
				out <- num
			}
		}
	}()

	return out
}

func Multiply(in <-chan int) int {
	result := 1

	for num := range in {
		result *= num
	}

	return result
}

func main() {
	nums := [][]int{
		{1, 2, 3, 4, 5},
		{1, 2, 1},
	}

	result := MultiplyPipeline(nums...)
	fmt.Println(result)
}
