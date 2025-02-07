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
