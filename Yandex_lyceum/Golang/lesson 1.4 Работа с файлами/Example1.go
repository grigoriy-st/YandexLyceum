package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	f, err := os.Open("first.txt")
	if err != nil {
		fmt.Println("Error")
	}
	fileScanner := bufio.NewScanner(f)
	for fileScanner.Scan() {
		fmt.Println(fileScanner.Text())
	}
}
