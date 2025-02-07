package main

import (
	"fmt"
	"math"
	"time"
)

func is_prime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func GeneratePrimeNumbers(
	stop chan struct{}, prime_nums chan int, N int) {

	go func() {
		for i := 2; i < N; i++ {
			if is_prime(i) {
				prime_nums <- i
			}
		}
	}()

	timer := time.NewTimer(10 * time.Millisecond)

	for {
		select {
		case prime, ok := <-prime_nums:
			if ok {
				fmt.Println(prime)
			}
		case <-timer.C:
			close(prime_nums)
			close(stop)
			return
		}
	}
}

func main() {
	// N := 100
	// stop := make(chan struct{})
	// prime_nums := make(chan int)
	// expectedPrimesUpTo20 := []int{2, 3, 5, 7, 11, 13, 17, 19}
	stop := make(chan struct{})
	primeChan := make(chan int)
	go GeneratePrimeNumbers(stop, primeChan, 20)

	<-stop
}
