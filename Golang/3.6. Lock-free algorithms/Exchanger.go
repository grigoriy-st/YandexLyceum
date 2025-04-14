package main

import (
	"fmt"
	"sync/atomic"
)

func AtomicSwap(a *int64, b *int64) {
	for {
		aValue := atomic.LoadInt64(a)
		bValue := atomic.LoadInt64(b)

		if atomic.CompareAndSwapInt64(a, aValue, bValue) {
			atomic.StoreInt64(b, aValue)
			break
		}
	}
}

func main() {
	var a int64 = 3
	var b int64 = 4

	AtomicSwap(&a, &b)

	fmt.Println(a, b)
}
