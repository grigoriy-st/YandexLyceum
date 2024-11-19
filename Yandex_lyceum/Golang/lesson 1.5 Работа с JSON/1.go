package main

import (
	"encoding/json"
)

type Student struct {
	Name  string `json:"name"`
	Grade int    `json:"grade"`
}

func modifyJSON(jsonData []byte) ([]byte, error) {
	var students []Student
	err := json.Unmarshal(jsonData, &students)
	if err != nil {
		return nil, err
	}
	for student := range students {
		students[student].Grade += 1
	}

	res, err := json.Marshal(students)
	if err != nil {
		return nil, err
	}
	return res, nil

}

func main() {
	data := []byte(`[{"name": "Alice", "grade": 10}, {"name": "Bob", "grade": 11}]`)
	modifyJSON(data)

}
