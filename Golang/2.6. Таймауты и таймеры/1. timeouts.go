package main

import (
	"fmt"
	"net/http"
)

func FetchURL(url string) string {
	resp, err := http.Get(url)
	if err != nil {
		return "Failed to fetch"
	}
	defer resp.Body.Close()

	if resp.StatusCode == http.StatusOK {
		return "Successfully fetched"
	}
	return "Failed to fetch"
}

func main() {

	url := "https://vk.com"
	res := FetchURL(url)
	fmt.Println(res)
}
