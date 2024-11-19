package main

import (
	"bytes"
	"encoding/json"
	"fmt"
)

type Student struct {
	Name  string `json:"name"`
	Age   int    `json:"age"`
	Grade int    `json:"grade"`
}

func main() {
	students := []Student{
		{Name: "Alice", Age: 12, Grade: 7},
		{Name: "Bob", Age: 13, Grade: 8},
		{Name: "Charlie", Age: 14, Grade: 9},
	}

	var buf bytes.Buffer

	encoder := json.NewEncoder(&buf)
	err := encoder.Encode(students)
	if err != nil {
		return
	}

	fmt.Println(buf.String())

}
