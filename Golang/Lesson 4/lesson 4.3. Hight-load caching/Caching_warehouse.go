package main

import (
	"errors"
	"sync"
	"time"
)

type Product struct {
	ID    int
	Name  string
	Price float64
	Stock int
}

type Cache struct {
	products map[int]cachedProduct
	ttl      time.Duration
	mu       sync.RWMutex
}

type cachedProduct struct {
	product   Product
	timestamp time.Time
}

func NewCache() *Cache {
	return &Cache{
		products: make(map[int]cachedProduct),
		ttl:      5 * time.Second,
	}
}

func (c *Cache) Get(productId int) (Product, bool) {
	c.mu.RLock()
	defer c.mu.RUnlock()
	if cached, found := c.products[productId]; found {
		if time.Since(cached.timestamp) < c.ttl {
			return cached.product, true
		}
		delete(c.products, productId)
	}
	return Product{}, false
}

func (c *Cache) Set(productId int, product Product) {
	c.mu.Lock()
	defer c.mu.Unlock()
	c.products[productId] = cachedProduct{product: product, timestamp: time.Now()}
}

func (c *Cache) Invalidate(productId int) {
	c.mu.Lock()
	defer c.mu.Unlock()
	delete(c.products, productId)
}

func getProduct(productId int, db map[int]Product, cache *Cache) (Product, error) {
	if product, found := cache.Get(productId); found {
		return product, nil
	}
	if product, found := db[productId]; found {
		cache.Set(productId, product)
		return product, nil
	}
	return Product{}, errors.New("product not found")
}

func updateProduct(productId int, newProduct Product, db map[int]Product) error {
	if _, exists := db[productId]; !exists {
		return errors.New("product not found in database")
	}
	db[productId] = newProduct
	return nil
}
