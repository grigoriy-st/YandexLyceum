package main

import (
	"fmt"
	"sync"
)

type Сount interface{  
	Increment()    // увеличение счётчика на единицу
	GetValue() int // получение текущего значения
}

type Counter struct {
	value int // значение счетчика
	mu    sync.RWMutex
}

func (c *Counter) GetValue() int {
	return c.value
}

func NewCounter() *Counter {
	return &Counter{
		value: 0,
	}
}

func main() {
	counter := NewCounter()

	fmt.Println(counter.GetValue())
}
