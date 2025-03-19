package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"net/http"
	"sync"
	"time"
)

type APIResponse struct {
	URL        string
	Data       string
	StatusCode int
	Err        error
}

func FetchAPI(ctx context.Context, urls []string, timeout time.Duration) []*APIResponse {
	var wg sync.WaitGroup
	responses := make([]*APIResponse, len(urls))
	ctx, cancel := context.WithTimeout(ctx, timeout)
	defer cancel()

	for i, url := range urls {
		wg.Add(1)
		go func(i int, url string) {
			defer wg.Done()
			req, err := http.NewRequestWithContext(ctx, http.MethodGet, url, nil)
			if err != nil {
				responses[i] = &APIResponse{URL: url, Err: err}
				return
			}

			resp, err := http.DefaultClient.Do(req)
			if err != nil {
				responses[i] = &APIResponse{URL: url, Err: err}
				return
			}
			defer resp.Body.Close()

			body, err := ioutil.ReadAll(resp.Body)
			if err != nil {
				responses[i] = &APIResponse{URL: url, StatusCode: resp.StatusCode, Err: err}
				return
			}

			responses[i] = &APIResponse{
				URL:        url,
				Data:       string(body),
				StatusCode: resp.StatusCode,
				Err:        nil,
			}
		}(i, url)
	}

	wg.Wait()
	return responses
}

func main() {
	ctx := context.Background()
	urls := []string{
		"https://jsonplaceholder.typicode.com/posts/1",
		"https://jsonplaceholder.typicode.com/posts/2",
		"https://jsonplaceholder.typicode.com/posts/3",
	}
	timeout := 2 * time.Second

	responses := FetchAPI(ctx, urls, timeout)
	for _, response := range responses {
		if response.Err != nil {
			fmt.Printf("Error fetching %s: %v\n", response.URL, response.Err)
		} else {
			fmt.Printf("Fetched %s: %d bytes, Status Code: %d\n", response.URL, len(response.Data), response.StatusCode)
		}
	}
}
