package main

import (
	"sync"
	"testing"
)

func TestReverseString(t *testing.T) {
	slices := []string{
		"first",
		"second",
		"third",
	}

	expectedResult := []string{
		"tsrif",
		"dnoces",
		"driht",
	}

	var wg sync.WaitGroup
	wg.Add(len(slices))

	for i := 0; i < len(slices); i++ {
		go func(i int) {
			defer wg.Done()
			got := ReverseString(slices[i])
			if got != expectedResult[i] {
				t.Errorf("Error. Expected: %v, Got: %v", expectedResult[i], got)
			}
		}(i)
	}

	wg.Wait()
}
