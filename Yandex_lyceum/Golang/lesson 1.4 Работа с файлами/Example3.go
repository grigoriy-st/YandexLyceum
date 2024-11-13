package main

import (
	"fmt"
	"os"
)

func main() {
	err := os.WriteFile("./second.txt", []byte("hello, world!"), 0666)
	if err != nil {
		fmt.Println("Error")
	}

	f, err := os.Create("./printBye.txt")
	n, err := f.WriteString("Good bye!")
	line := "Записано строк" + fmt.Sprint(n) 
	fmt.Println(line)
	_, _ = f.Write("printBye.txt", []byte{line}, 0666)
	errClose := f.Close()
}
