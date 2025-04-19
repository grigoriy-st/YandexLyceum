package main

import (
	"sync"
)

type Cache struct {
	UpperBound int
	LowerBound int
	values     map[string]*entry
	frequency  map[int]*frequencyList
	minFreq    int
	lock       sync.Mutex
}

type entry struct {
	key   string
	value interface{}
	freq  int
}

type frequencyList struct {
	entries map[string]*entry
}

func New() *Cache {
	return NewWithBounds(0, 0)
}

func NewWithBounds(upperBound, lowerBound int) *Cache {
	return &Cache{
		UpperBound: upperBound,
		LowerBound: lowerBound,
		values:     make(map[string]*entry),
		frequency:  make(map[int]*frequencyList),
		minFreq:    0,
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
		c.Evict(1)
	}
	e := &entry{key: key, value: value, freq: 1}
	c.values[key] = e
	if _, exists := c.frequency[1]; !exists {
		c.frequency[1] = &frequencyList{entries: make(map[string]*entry)}
	}
	c.frequency[1].entries[key] = e
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
	if count <= 0 || c.LowerBound == 0 {
		return 0
	}
	removed := 0
	for len(c.values) > c.LowerBound && removed < count {
		if freqList, ok := c.frequency[c.minFreq]; ok {
			for key := range freqList.entries {
				delete(c.values, key)
				removed++
				if removed >= count {
					break
				}
			}
			delete(c.frequency, c.minFreq)
			c.minFreq++
			if len(c.frequency) == 0 {
				c.minFreq = 0
			}
		}
	}
	return removed
}

func (c *Cache) increment(e *entry) {
	oldFreq := e.freq
	e.freq++
	if freqList, ok := c.frequency[oldFreq]; ok {
		delete(freqList.entries, e.key)
		if len(freqList.entries) == 0 {
			delete(c.frequency, oldFreq)
			if oldFreq == c.minFreq {
				c.minFreq++
			}
		}
	}
	if _, ok := c.frequency[e.freq]; !ok {
		c.frequency[e.freq] = &frequencyList{entries: make(map[string]*entry)}
	}
	c.frequency[e.freq].entries[e.key] = e
}
