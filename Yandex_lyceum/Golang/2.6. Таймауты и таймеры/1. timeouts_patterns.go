package main

import "math"

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

func GeneratePrimeNumbers(stop chan struct{}, prime_nums chan int, N int) {
	defer close(prime_nums)

	if N <= 2 && N >= 105 {
		return
	}

	for i := 2; i <= N; i++ {
		select {
		case <-stop:
			return
		default:
			if isPrime(i) {
				prime_nums <- i
			}
		}
	}
}
