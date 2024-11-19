package main

import (
	"encoding/json"
	"fmt"
)

type Person struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	person := Person{Name: "John", Age: 10}
	jsonBytes, _ := json.Marshal(person)

	fmt.Println(string(jsonBytes))
}
