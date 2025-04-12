package main

import (
	"errors"
	"sync"
)

type Summer interface {
	ProcessSum(summer func(arr []int, result chan<- int), nums []int, chunkSize int) (int, error)
}

func ProcessSum(summer func(arr []int, result chan<- int), nums []int, chunkSize int) (int, error) {
	var wg sync.WaitGroup

	if chunkSize <= 0 {
		return 0, errors.New("bad chunk size")
	}

	numChunks := len(nums) / chunkSize
	if len(nums)%chunkSize > 0 {
		numChunks++
	}

	result := make(chan int, numChunks)

	var sum_arr []int
	for i, num := range nums {
		sum_arr = append(sum_arr, num)

		if len(sum_arr) == chunkSize || i == len(nums)-1 {
			wg.Add(1)
			go func(arr []int) {
				defer wg.Done()
				summer(arr, result)
			}(sum_arr)
			sum_arr = nil
		}
	}

	go func() {
		wg.Wait()
		close(result)
	}()

	sum := 0
	for r := range result {
		sum += r
	}

	return sum, nil
}

func SumChunk(arr []int, result chan<- int) {
	sum := 0
	for _, i := range arr {
		sum += i
	}
	result <- sum
}
