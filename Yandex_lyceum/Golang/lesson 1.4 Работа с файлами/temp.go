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

		// Проверяем, попадает ли дата в указанный диапазон (включительно)

		if parsedDate.Equal(start) || parsedDate.Equal(end) || (parsedDate.After(start) && parsedDate.Before(end)) {

			result = append(result, log)

		}

	}

	if err := scanner.Err(); err != nil {

		return nil, err

	}

	if len(result) == 0 {

		return nil, fmt.Errorf("no records found in the specified date range")

	}

	return result, nil

}

func main() {

	startTime := time.Date(2022, time.December, 13, 0, 0, 0, 0, time.UTC)

	endTime := time.Date(2022, time.December, 15, 0, 0, 0, 0, time.UTC)

	res, err := ExtractLog("log.txt", startTime, endTime)

	if err != nil {

		fmt.Println("Error:", err)

	} else {

		fmt.Println(res)

	}

}
