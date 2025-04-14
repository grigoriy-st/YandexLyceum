package main

import (
	"fmt"
	"time"
)

func timeoutTest() string {
	time.Sleep(4 * time.Second)
	return "Function TimeoutTest complited!"
}

func main() {
	c := make(chan string, 1)

	go func() {
		str := timeoutTest()
		c <- str
	}()

	select {
	case res := <-c:
		fmt.Println(res)
	case <-time.After(5 * time.Second):
		fmt.Println("Time is up")
	}
}
