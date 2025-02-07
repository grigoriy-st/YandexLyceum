package main

import (
	"fmt"
	"sync"
)

type Сount interface {
	Increment()    // увеличение счётчика на единицу
	GetValue() int // получение текущего значения
}

type Counter struct {
	value int // значение счетчика
	mu    sync.RWMutex
}

func (c *Counter) GetValue() int {
	c.mu.Lock()
	defer c.mu.Unlock()
	return c.value
}

func (c *Counter) Increment() {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.value++
}

func NewCounter() *Counter {
	return &Counter{
		value: 0,
	}
}

func main() {
	counter := NewCounter()
	counter.Increment()
	fmt.Println(counter.GetValue())
	counter.Increment()
	fmt.Println(counter.GetValue())
	counter.Increment()
	fmt.Println(counter.GetValue())
}
