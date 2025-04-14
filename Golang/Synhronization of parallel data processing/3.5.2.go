package main

import (
	"sync"
	"context"
)

type sequenced interface {
	getSequence() int
}

func EvenNumbersGen[T sequenced](ctx context.Context, numbers ...T) <-chan T {
	out := make(chan T)
	wg := sync.WaitGroup{}

	for _, num :+ range numbers{
		wg.Add()

		go func(n T) {
			defer close(out)

			if n.getSequence() % 2 == 0 {
				select {
				case out <- n:
				case <-ctx.Done():
					return
				}
			}
		}(num)
	}

	go func() {
		wg.Wait()
		close(out)
	}
}