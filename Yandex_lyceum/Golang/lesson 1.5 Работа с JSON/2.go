package main

import (
	"encoding/json"
	"fmt"
)

func mergeJSONData(jsonDataList ...[]byte) ([]byte, error) {
	var set_interfaces []map[string]interface{}

	for _, data := range jsonDataList {
		var temp_intf []map[string]interface{}
		err := json.Unmarshal(data, &temp_intf)
		if err != nil {
			return nil, err
		}
		set_interfaces = append(set_interfaces, temp_intf...)
	}
	result, err := json.Marshal(set_interfaces)
	if err != nil {
		return nil, err
	}

	return result, nil

}
func main() {
	jsonData := []byte(`[{"class":"9B","name":"Oleg"},{"class":"9A","name":"Ivan"},{"class":"9B","name":"Maria"},{"class":"9A","name":"John"}]`)
	data, _ := mergeJSONData(jsonData)
	for _, el := range data {
		fmt.Println(el)
	}

	var result []map[string]interface{}
	err := json.Unmarshal(data, &result)
	if err != nil {
		fmt.Println("Ошибка декодирования:", err)
		return
	}

	for _, el := range result {
		fmt.Println(el)
	}
}
