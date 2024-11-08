package main

import "fmt"

type Book struct {
	Title  string
	Author string
	Year   int
	Genre  string
}

func NewBook(title, author string, year int, genre string) *Book {
	return &Book{
		Title:  title,
		Author: author,
		Year:   year,
		Genre:  genre,
	}
}

func main() {
	fmt.Print()
}
