package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func NumbersGen(filename string) <-chan int {
	out := make(chan int)

	go func() {
		defer close(out)

		file, err := os.Open(filename)
		if err != nil {
			log.Fatal(err)
		}
		defer file.Close()

		scanner := bufio.NewScanner(file)

		for scanner.Scan() {
			line := scanner.Text()
			num, err := strconv.Atoi(line)
			if err != nil {
				continue
			}
			out <- num
		}

		if err := scanner.Err(); err != nil {
			log.Fatal(err)
		}
	}()

	return out
}

func main() {
	nums := NumbersGen("file.txt")

	for num := range nums {
		fmt.Println(num)
	}
}
