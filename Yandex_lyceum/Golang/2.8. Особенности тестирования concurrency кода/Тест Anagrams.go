package main

import (
	"sync"
	"testing"
)

func TestAreAnagrams(t *testing.T) {
	slice := [][]string{
		{"hello", "olloeh"},
		{"malo", "morlo"},
		{"first", "tsrif"},
	}

	expectedResults := []bool{
		true,
		false,
		true,
	}

	var wg sync.WaitGroup
	wg.Add(len(slice))

	for i := 0; i < len(slice); i++ {
		go func(i int) {
			defer wg.Done()
			got := AreAnagrams(slice[i][0], slice[i][1])
			if got != expectedResults[i] {
				t.Errorf("Error. Expected: %v, Got: %v", expectedResults[i], got)
			}
		}(i)
	}

	wg.Wait()
}
