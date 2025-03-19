package main

import (
	"sync"
	"testing"
)

func TestContains(t *testing.T) {
	target := 3

	slices := [][]int{
		{1, 2, 3, 4, 5},
		{3, 3, 3},
		{7, 8, 9},
	}
	expectedResults := []bool{
		true,
		true,
		false,
	}

	var wg sync.WaitGroup
	wg.Add(len(slices))

	for i := 0; i < len(slices); i++ {
		go func(i int) {
			defer wg.Done()
			got := Contains(slices[i], target)
			if got != expectedResults[i] {
				t.Errorf("Error. Expected: %v, Got: %v", expectedResults[i], got)
			}
		}(i)
	}

	wg.Wait()
}
