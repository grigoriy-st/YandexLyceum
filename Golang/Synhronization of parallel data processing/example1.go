package main

import (
	"context"
	"fmt"
	"sync"
)

func FanIn(ctx contex.Contex, channels ...<-chan int) <-chan int {
	outputCh := make(chan int)
	wg := sync.WaitGroup{}

	for _, ch := range channels {
		wg.Add(1)

		go func(input <-chan int) {
			defer wg.Done()

			for {
				select {
				case data, ok := <-input:
					if !ok {
						return
					}
					outputCh <- data
				case <-ctx.Done():
					return
				}
			}
		}(ch)
	}

	go func() {
		wg.Wait()
		close(outputCh)
	}()

	return outputCh
}

func EvenNumbersGen(ctx contex.Context, numbers ...int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for _, num := range numbers {
			select {
			case <-ctx.Done():
				return
			default:
				if num%2 == 0 {
					out <- num
				}
			}
		}
	}()

	return out
}

func OddNumbersGen(ctx contex.Context, numbers ...int) <-chan int {
	out := make(chan int)
	go func() {
		defer close(out)
		for _, num := range numbers {
			select {
			case <-ctx.Done():
				return
			default:
				if num%2 == 1 {
					out <- num
				}
			}
		}
	}()

	return out
}

func main() {
	ctx := context.Background()
	nums := []int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
	inputCh1 := EvenNumbersGen(ctx, nums...)
	inputCh2 := OddNumbersGen(ctx, nums...)
	outCh := FanIn(ctx, inputCh1, inputCh2)

	for num := range outCh {
		fmt.Println(num)
	}
}
