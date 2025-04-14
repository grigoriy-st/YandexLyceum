package main

import (
	"fmt"
	"sync/atomic"
)

func AtomicSwap(a *int32, b *int32) {
	for {
		aValue := atomic.LoadInt32(a)
		bValue := atomic.LoadInt32(b)

		if atomic.CompareAndSwapInt32(a, aValue, bValue) {
			atomic.StoreInt32(b, aValue)
			break
		}
	}
}

func main() {
	var a int32 = 3
	var b int32 = 4

	AtomicSwap(&a, &b)

	fmt.Println(a, b)
}
