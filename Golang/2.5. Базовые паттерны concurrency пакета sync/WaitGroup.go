package main

import (
	"fmt"
	"math/rand"
	"sync"
)

type SafeSlice struct {
	results []int
	mx      *sync.Mutex
}

func New() *SafeSlice {
	return &SafeSlice{
		mx:      &sync.Mutex{},
		results: []int{},
	}
}

func (s *SafeSlice) Append(item int) {
	s.mx.Lock()
	defer s.mx.Unlock()

	s.results = append(s.results, random())
}

func (s *SafeSlice) Get(index int) int {
	s.mx.Lock()
	defer s.mx.Unlock()
	return s.results[index]
}

func random() int {
	const max int = 100
	return rand.Intn(max)
}

func main() {
	safeSlice := New()

	const size int = 10
	wg := &sync.WaitGroup{}

	for i := 0; i < size; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			safeSlice.Append(random())
		}()
	}

	wg.Wait()

	for i := 0; i < size; i++ {
		fmt.Println(safeSlice.Get(i))
	}
}
