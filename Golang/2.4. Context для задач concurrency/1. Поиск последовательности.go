<<<<<<< HEAD
package main

import (
	"bytes"
	"context"
	"errors"
	"io"
)

func Contains(ctx context.Context, r io.Reader, seq []byte) (bool, error) {
	seqLen := len(seq)
	if seqLen == 0 {
		return false, errors.New("Error")
	}

	buffer := make([]byte, 4096)
	var lastBytes []byte

	for {
		select {
		case <-ctx.Done():
			return false, ctx.Err()
		default:
			n, err := r.Read(buffer)
			if err != nil {
				if err == io.EOF {
					if bytes.Contains(append(lastBytes, buffer[:n]...), seq) {
						return true, nil
					}
					return false, nil
				}
				return false, err
			}

			if bytes.Contains(append(lastBytes, buffer[:n]...), seq) {
				return true, nil
			}

			if n >= seqLen {
				lastBytes = buffer[n-seqLen+1 : n]
			} else {
				lastBytes = append(lastBytes[:0], buffer[:n]...)
			}
		}

	}
}
=======
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
>>>>>>> 787d77b7ad4dd9c0044702f3ca685a72d1b8abff
