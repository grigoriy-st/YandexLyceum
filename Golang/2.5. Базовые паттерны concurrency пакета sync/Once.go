package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	wg := &sync.WaitGroup{}
	initializeResources := func() {
		time.Sleep(time.Second)
		fmt.Println("Only once initialize something")
	}

	for i := 0; i < 10; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			initializeResources()
		}()
	}
	wg.Wait()
}
