package main

import (
	"bufio"
	_ "compress/gzip"
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	filename := "command-line-arguments.test"

	file, err := os.Open(filename)
	if err != nil {
		fmt.Println("Ошибка при открытии файла:", err)
		return
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			fmt.Println(line)
		}
	}
	//
	files, err := ioutil.ReadDir(".")
	if err != nil {
		log.Fatal(err)
	}

	var names []string
	for _, f := range files {
		names = append(names, f.Name())
	}

	fmt.Println(names)
}
