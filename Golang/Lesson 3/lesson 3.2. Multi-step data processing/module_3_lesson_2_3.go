package main

import (
	"encoding/csv"
	"fmt"
	"os"
)

func ReadCSV(file string) (<-chan []string, error) {
	out := make(chan []string)

	f, err := os.Open(file)
	if err != nil {
		return nil, err
	}

	go func() {
		defer close(out)
		defer f.Close()

		reader := csv.NewReader(f)

		for {
			record, err := reader.Read()
			if err != nil {
				if err == csv.ErrFieldCount {
					fmt.Println("Error:", err)
					return
				}
				break
			}
			out <- record
		}
	}()

	return out, nil
}
