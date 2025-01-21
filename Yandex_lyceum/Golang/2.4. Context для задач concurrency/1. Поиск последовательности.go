package main

import (
	"bytes"
	"context"
	"fmt"
	"io"
	"strings"
)

func Contains(ctx context.Context, r io.Reader, seq []byte) (bool, error) {
	buf := make([]byte, 4096)
	var data []byte

	for {
		select {
		case <-ctx.Done():
			return false, ctx.Err()
		default:
		}

		n, err := r.Read(buf)

		if err != nil {
			if err == io.EOF {
				break
			}
			return false, err
		}

		data = append(data, buf[:n]...)

		if bytes.Contains(seq) {
			return true, nil
		}
	}
	return false, nil
}

func main() {
	ctx := context.Background()

	data := "Hello, world!"
	reader := strings.NewReader(data)

	seq := []byte("world")

	found, err := Contains(ctx, reader, eq)
	if err != nil {
		fmt.Println("error:", err)
	} else if found {
		fmt.Println("Sequence found!")
	} else {
		fmt.Println("Sequence not found.")
	}
}
