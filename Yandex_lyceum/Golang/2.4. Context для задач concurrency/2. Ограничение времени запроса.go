package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"
)

type APIResponse struct {
	Data       string
	StatusCode int
}

func fetchAPI(ctx context.Context,
	url string, timeout time.Duration) (*APIResponse, error) {

	ctx, cansel := context.WithTimeout(ctx, timeout)
	defer cansel()

	req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
	if err != nil {
		return nil, err
	}

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		return nil, err
	}

	return &APIResponse{
		Data:       string(body),
		StatusCode: resp.StatusCode,
	}, nil
}

func main() {
	ctx := context.Background()
	url := "https://www.quickpickdeal.com/api/Auth/GetBearerToken"
	timeout := 5 * time.Second

	response, err := fetchAPI(ctx, url, timeout)
	if err != nil {
		if err == context.DeadlineExceeded {
			fmt.Println("Запрос превысил таймаут")
		} else {
			fmt.Println("Error")
		}
		return
	}

	fmt.Println("Response code: %d", response.StatusCode)
}
