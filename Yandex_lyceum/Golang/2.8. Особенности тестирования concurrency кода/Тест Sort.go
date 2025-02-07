package main

import (
	"sync"
	"testing"
)

func TestSortIntegers(t *testing.T) {
	test_slices := [][]int{
		{3, 1, 4, 2, 5},
		{6, 4, 2, 5, 7},
		{1, 10, 5, 3},
	}

	correct_seq_slices := [][]int{
		{1, 2, 3, 4, 5},
		{2, 4, 5, 6, 7},
		{1, 3, 5, 10},
	}

	var wg sync.WaitGroup

	wg.Add(len(test_slices))

	for i := 0; i < len(test_slices); i++ {
		go func(i int) {
			defer wg.Done()
			SortIntegers(test_slices[i])

			for j := range test_slices[i] {
				if test_slices[i][j] != correct_seq_slices[i][j] {
					t.Errorf("Error. Expected: %v, Got:%v", correct_seq_slices[i], test_slices[i])
				}
			}
		}(i)
	}

	wg.Wait()

}
