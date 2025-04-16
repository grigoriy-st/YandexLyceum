// MRU (most recently used) cache. В случае если при установке элемента достигнуто максимальное значение размера кеша, то удаляем из кэша последний использованный элемент.

package main

import "fmt"

type Node struct {
	key   string
	value string
	prev  *Node
	next  *Node
}

// структура MRU кеша
type MRUCache struct {
	capacity int
	cache    map[string]*Node
	head     *Node
	tail     *Node
}

// возвращает новый инстанс кеша размером capacity
func NewMRUCache(capacity int) *MRUCache {
	return &MRUCache{
		capacity: capacity,
		cache:    make(map[string]*Node),
		head:     nil,
		tail:     nil,
	}
}

// устанавливает значени value ключу key
func (c *MRUCache) Set(key, value string) {
	if c.head == node {
		return
	}

	if node.prev != nil {
		node.prev.next = node.next
	}

	if node.next != nil {
		node.next.prev = node.prev
	}

	if c.tail != node {
		c.tail = node.prev
	}

	node.prev = nil
	node.next = c.head
	if c.head != nil {
		c.head.prev = node
	}

	c.head = node
	if c.tail == nil {
		c.tail = node
	}
}

// получает значение и флаг его начличия по ключу key
func (c *MRUCache) Get(key string) (string, bool) {

}

func main() {
	fmt.Println("vim-go")
}
