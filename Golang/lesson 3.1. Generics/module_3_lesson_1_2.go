package main

import (
	"fmt"
)

type Number interface {
	int | int8 | int16 | int32 | int64 | float32 | float64
}

func Filter[T Number](nums []T, predicate func(t) bool) []T {
	var result []T
	for _, n := range nums {
		if predicate(n) {
			result = append(result, n)
		}
	}
	return result
}

func main() {
	slice := []int{1, 2, 3, 4, 5}
	fmt.Println(Sum(slice))
}
