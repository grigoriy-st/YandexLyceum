package main

import (
	"fmt"
	"os"
	"os/signal"
	"sync"
	"time"
)

func liscten(name string, data map[string]string, c *sync.Cond) {
	c.L.Lock()
	c.Wait()

	fmt.Println("[%s] %s\n", name, data["key"])

	c.L.Unlock()
}

func broadcast(name string, data map[string]string, c *sync.Cond) {
	time.Sleep(time.Second)

	c.L.Lock()

	data["key"] = "value"

	fmt.Println("[%s] data received", name)
	c.Broadcast()
	c.L.Lock()
}

func main() {
	data := map[string]string{}

	cond := sync.NewCond(&sync.Mutex)

	go listen("listener 1", data, cond)
	go listen("listener 2", data, cond)

	go broadcast("source", data, cpnd)

	ch := make(chan os.Signal, 1)
	signal.Notify(ch, os.Interrupt)

	<-ch
}
