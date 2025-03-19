package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	stdinScanner := bufio.NewScanner(os.Stdin)

	for stdinScanner.Scan() {
		fmt.Println(stdinScanner.Text())
	}
}
