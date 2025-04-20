package main

import (
	"container/list"
	"sync"
)

type Cache struct {
	UpperBound int
	LowerBound int

	values    map[string]*cacheEntry
	freqLists map[int]*list.List
	minFreq   int
	lock      sync.Mutex
}

type cacheEntry struct {
	key       string
	value     interface{}
	freq      int
	listElem  *list.Element
}

func New() *Cache {
	return &Cache{
		values:    make(map[string]*cacheEntry),
		freqLists: make(map[int]*list.List),
		minFreq:   1,
	}
}

func (c *Cache) Has(key string) bool {
	c.lock.Lock()
	defer c.lock.Unlock()
	_, exists := c.values[key]
	return exists
}

func (c *Cache) Get(key string) interface{} {
	c.lock.Lock()
	defer c.lock.Unlock()
	if e, ok := c.values[key]; ok {
		c.increment(e)
		return e.value
	}
	return nil
}

func (c *Cache) Set(key string, value interface{}) {
	c.lock.Lock()
	defer c.lock.Unlock()

	if e, exists := c.values[key]; exists {
		e.value = value
		c.increment(e)
		return
	}

	if c.UpperBound > 0 && len(c.values) >= c.UpperBound {
		target := c.LowerBound
		if target <= 0 {
			target = c.UpperBound - 1
		}
		c.evictToSize(target)
	}

	e := &cacheEntry{
		key:   key,
		value: value,
		freq:  1,
	}

	if c.freqLists[1] == nil {
		c.freqLists[1] = list.New()
	}
	e.listElem = c.freqLists[1].PushFront(e)
	c.values[key] = e
	c.minFreq = 1
}

func (c *Cache) Len() int {
	c.lock.Lock()
	defer c.lock.Unlock()
	return len(c.values)
}

func (c *Cache) GetFrequency(key string) int {
	c.lock.Lock()
	defer c.lock.Unlock()
	if e, ok := c.values[key]; ok {
		return e.freq
	}
	return 0
}

func (c *Cache) Keys() []string {
	c.lock.Lock()
	defer c.lock.Unlock()
	keys := make([]string, 0, len(c.values))
	for k := range c.values {
		keys = append(keys, k)
	}
	return keys
}

func (c *Cache) Evict(count int) int {
	c.lock.Lock()
	defer c.lock.Unlock()
	return c.evict(count)
}

func (c *Cache) increment(e *cacheEntry) {
	currentList := c.freqLists[e.freq]
	currentList.Remove(e.listElem)

	if e.freq == c.minFreq && currentList.Len() == 0 {
		c.minFreq++
	}

	e.freq++

	if c.freqLists[e.freq] == nil {
		c.freqLists[e.freq] = list.New()
	}
	e.listElem = c.freqLists[e.freq].PushFront(e)
}

func (c *Cache) evict(count int) int {
	removed := 0
	for i := 0; i < count && len(c.values) > 0; i++ {
		list := c.freqLists[c.minFreq]
		if list == nil || list.Len() == 0 {
			c.minFreq++
			i--
			continue
		}

		back := list.Back()
		if back == nil {
			c.minFreq++
			i--
			continue
		}

		e := back.Value.(*cacheEntry)
		list.Remove(back)
		delete(c.values, e.key)
		removed++
	}

	for c.minFreq <= 1 || (c.freqLists[c.minFreq] != nil && c.freqLists[c.minFreq].Len() > 0) {
		if c.freqLists[c.minFreq] != nil && c.freqLists[c.minFreq].Len() > 0 {
			break
		}
		c.minFreq++
	}

	return removed
}

func (c *Cache) evictToSize(target int) int {
	if target >= len(c.values) {
		return 0
	}
	return c.evict(len(c.values) - target)
}