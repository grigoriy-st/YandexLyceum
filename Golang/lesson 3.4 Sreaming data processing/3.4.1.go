package main

import "fmt"

func StringsGen(lines ...string) <-chan string {
	out := make(chan string)
	go func() {
		defer close(out)

		for line := range lines {
			fmt.Println(i)
			out <- line
		}
	}()

	return out
}

func main() {
	strings := StringsGen("Hello", ",", "world")

	for t_string := range strings {
		fmt.Println(t_string)
	}
}
