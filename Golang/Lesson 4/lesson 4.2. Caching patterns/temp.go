package main

type Node struct {
	key   string
	value string
	prev  *Node
	next  *Node
}

type MRUCache struct {
	capacity int
	cache    map[string]*Node
	head     *Node
	tail     *Node
}

func NewMRUCache(capacity int) *MRUCache {
	return &MRUCache{
		capacity: capacity,
		cache:    make(map[string]*Node),
		head:     nil,
		tail:     nil,
	}
}

func (c *MRUCache) moveToHead(node *Node) {
	if c.head == node {
		return
	}
	if node.prev != nil {
		node.prev.next = node.next
	}
	if node.next != nil {
		node.next.prev = node.prev
	}
	if c.tail == node {
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
func (c *MRUCache) Set(key, value string) {
	if node, exists := c.cache[key]; exists {
		node.value = value
		c.moveToHead(node)
		return
	}
	if len(c.cache) >= c.capacity {
		if c.tail != nil {
			delete(c.cache, c.tail.key)
			c.tail = c.tail.prev
			if c.tail != nil {
				c.tail.next = nil
			}
		}
	}
	newNode := &Node{key: key, value: value}
	c.cache[key] = newNode
	c.moveToHead(newNode)
}

func (c *MRUCache) Get(key string) (string, bool) {
	if node, exists := c.cache[key]; exists {
		c.moveToHead(node)
		return node.value, true
	}
	return "", false
}
