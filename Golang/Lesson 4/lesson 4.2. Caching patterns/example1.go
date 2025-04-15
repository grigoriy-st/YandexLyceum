package main

import (
	"fmt"
	"sync"
	"time"
)

type Cache struct {
	data  map[string]interface{}
	mutex sync.RWMutex
}

func NewCache() *Cache {
	return &Cache{
		data: make(map[string]interface{}),
	}
}

func (c *Cache) Get(key string) (interface{}, bool) {
	c.mutex.RLock()
	defer c.mutex.RUnlock()
	value, ok := c.data[key]
	return value, ok
}

func (c *Cache) Set(key string, value interface{}) {
	c.mutex.Lock()
	defer c.mutex.Unlock()
	c.data[key] = value
}

func main() {
	cache := NewCache()

	cache.Set("username", "grigoriy")
	cache.Set("year", 19)

	if value, ok := cache.Get("username"); ok {
		fmt.Println("Success:", value)
	} else {
		fmt.Println("Error")
	}

	time.Sleep(2 * time.Second)

	if value, ok := cache.Get("year"); ok {
		fmt.Println("Success", value)
	} else {
		fmt.Println("Error")
	}
}
