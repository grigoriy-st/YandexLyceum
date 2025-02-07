package main

import (
	"fmt"
	"time"
)

func timersStoppage(v time.Timer) {
	<-v.C
	fmt.Println("Second timer went off")
}
func main() {
	timer := time.NewTicker(3 * time.Second)

	<-timer.C
	fmt.Println("Time is up")

	timer_s := time.NewTimer(time.Second)

	go timersStoppage(*timer_s)

	stop_s := timer_s.Stop()
	if stop_s {
		fmt.Println("Second times is stopped")
	}
}
