package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

func SumValuesPipeline(filename string) int {
	nums := NumbersGen(filename)
	filtered := Filter(nums)
	return Sum(filtered)
}

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

func Filter(in <-chan int) <-chan int {
	out := make(chan int)

	go func() {
		defer close(out)

		for num := range in {
			if num%2 == 0 {
				out <- num
			}
		}
	}()

	return out
}

func Sum(in <-chan int) int {
	out := 0

	for el := range in {
		out += el
	}

	return out
}

func main() {
	result := SumValuesPipeline("file.txt")
	fmt.Println(result)
	fmt.Println("hello")
}
