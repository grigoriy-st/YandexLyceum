package main

import (
	"fmt"
	"os"
)

func ReadContent(filename string) string {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
	}
	return string(content)

}

func main() {
	fmt.Println(ReadContent("third.txt"))
}
