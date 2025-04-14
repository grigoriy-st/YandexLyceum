package main

import (
	"log"
	"os"
)

func WriteToLogFile(message string, fileName string) error {
	file, err := os.OpenFile(fileName, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0644)
	if err != nil {
		return nil
	}
	defer file.Close()
	log.SetOutput(message)
	log.Println("hello world")
	return nil
}

func main() {
	WriteToLogFile("hello, world", "output.txt")
}
