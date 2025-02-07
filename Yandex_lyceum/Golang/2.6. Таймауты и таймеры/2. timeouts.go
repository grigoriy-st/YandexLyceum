package main

import (
	"errors"
	"fmt"
	"time"
)

func Fib(n int) int {
	if n <= 0 {
		return 0
	} else if n == 1 {
		return 1
	}
	return Fib(n-1) + Fib(n-2)
}

func TimeoutFibonacci(n int, timeout time.Duration) (int, error) {
	c := make(chan int, 1)

	go func() {
		num := Fib(n)
		c <- num
	}()

	select {
	case res := <-c:
		return res, nil
	case <-time.After(timeout):
		return 0, errors.New("Error")
	}
}

func main() {
	n := 10
	timeout := 2 * time.Second

	result, err := TimeoutFibonacci(n, timeout)
	if err != nil {
		fmt.Println("err")
	} else {
		fmt.Println("Fib:", result)
	}
}
