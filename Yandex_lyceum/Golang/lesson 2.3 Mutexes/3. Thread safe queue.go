package main

import "sync"

type ConcurrentQueue struct {
	queue []interface{} // здесь хранить элементы очереди
	mutex sync.Mutex
}

type Queue interface {
	Enqueue(element interface{}) // положить элемент в очередь
	Dequeue() interface{}        // забрать первый элемент из очереди
}

func (c *ConcurrentQueue) Enqueue(element interface{}) {
	c.mutex.Lock()
	defer c.mutex.Unlock()

	c.queue = append(c.queue, element)
}

func (c *ConcurrentQueue) Dequeue() interface{} {
	c.mutex.Lock()
	defer c.mutex.Unlock()

	temp := c.queue[len(c.queue)-1]
	c.queue = c.queue[:len(c.queue)-1]

	return temp
}

func main() {

}
