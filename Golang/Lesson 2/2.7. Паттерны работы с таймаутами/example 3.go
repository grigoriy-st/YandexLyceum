// Паттерн для параллельных запросов с тайм-аутом

package main

import (
	"fmt"
	"net/http"
	"time"
)

func fetchURL(url string, c chan string) {
	client := http.Client{
		Timeout: 5 * time.Second,
	}
	resp, err := client.Get(url)
	if err != nil {
		c <- fmt.Sprintf("Error: %s : %s", url, err)
		return
	}
	defer resp.Body.Close()
	c <- fmt.Sprintf("Answer: %s. Status: %s", url, resp.Status)
}

func main() {
	urls := []string{
		"https://ya.ru",
		"https://lyceum.yandex.ru",
		"https://ihumaunkabir.com/", // with error
	}

	c := make(chan string, len(urls))
	for _, url := range urls {
		go fetchURL(url, c)
	}

	timeout := time.After(15 * time.Second)

	for i := 0; i < len(urls); i++ {
		select {
		case result := <-c:
			fmt.Println(result)
		case <-timeout:
			fmt.Println("Time's up")
			return

		}

	}

}
