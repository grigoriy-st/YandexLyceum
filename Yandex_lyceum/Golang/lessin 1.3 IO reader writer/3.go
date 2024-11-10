package main

import (
	"fmt"
	"strings"
)

type UpperWriter struct {
	UpperString string
}

func (uw *UpperWriter) Write(s []byte) (n int, err error) {
	upperStr := strings.ToUpper(string(s))
	uw.UpperString += upperStr
	return len(s), nil
}

func main() {
	var uw UpperWriter
	_, err := uw.Write([]byte("hello, world"))
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	fmt.Println(uw.UpperString) // Output: HELLO, WORLD

	return
}
