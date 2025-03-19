package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"time"
)

func ExtractLog(inputFileName string, start, end time.Time) ([]string, error) {
	file, err := os.Open(inputFileName)
	if err != nil {
		return nil, err
	}

	defer file.Close()

	result := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		log := scanner.Text()
		dateStr := strings.Split(log, " ")[0]

		parsedDate, err := time.Parse("02.01.2006", dateStr)
		if err != nil {
			return nil, err
		}

		if (parsedDate.Equal(start) || parsedDate.Equal(end)) ||
			(parsedDate.After(start) && parsedDate.Before(end)) {
			result = append(result, log)

		}
	}

	if len(result) != 0 {
		return result, nil
	}

	return []string{}, fmt.Errorf("Not found records")

}

func main() {
	start_time := time.Date(2022, 12, 19, 0, 0, 0, 0, time.UTC)
	end_time := time.Date(2022, 12, 20, 0, 0, 0, 0, time.UTC)
	res, _ := ExtractLog("log2.txt", start_time, end_time)
	fmt.Println(res)
}
