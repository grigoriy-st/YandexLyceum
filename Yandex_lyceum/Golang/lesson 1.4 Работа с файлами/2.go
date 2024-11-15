package main

import (
	"bufio"
	"fmt"
	"os"
)

func LineByNum(inputFilename string, lineNum int) string {

	file, err := os.Open(inputFilename)
	if err != nil {
		return ""
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	curLine := 0

	for scanner.Scan() {
		if curLine == lineNum {
			return scanner.Text()
		}
		curLine++
	}
	err = scanner.Err()
	if err != nil {
		return ""
	}
	return ""
}

func main() {
	fmt.Println(LineByNum("fourth.txt", 1))
}
