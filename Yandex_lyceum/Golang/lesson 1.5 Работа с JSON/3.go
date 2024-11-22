package main

import (
	"encoding/json"
	"fmt"
)

func splitJSONByClass(jsonData []byte) (map[string][]byte, error) {
	var data []map[string]interface{}

	err := json.Unmarshal(jsonData, &data)
	if err != nil {
		return nil, err
	}

	sortedData := make(map[string][]map[string]interface{})

	for _, el := range data {
		class := el["class"].(string)
		sortedData[class] = append(sortedData[class], el)
	}

	result := make(map[string][]byte)

	for key, val := range sortedData {
		jsonBytes, _ := json.Marshal(val)
		if err != nil {
			return nil, err
		}
		result[key] = jsonBytes
	}

	return result, nil
}

func main() {
	jsonData := []byte(`[
	{"class":"9B", "name":"Oleg"}, 
	{"class":"10A", "name":"Grigoriy"},
	{"class":"8A", "name":"Max"}
	]`)

	data, err := splitJSONByClass(jsonData)
	if err != nil {
		fmt.Println(err)
	}
	for key, val := range data {
		fmt.Println(string(key), string(val))
	}
}
