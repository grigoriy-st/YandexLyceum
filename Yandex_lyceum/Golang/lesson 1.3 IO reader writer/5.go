package main

import (
	"bytes"
	"errors"
	"io"
)

func Contains(r io.Reader, seq []byte) (bool, error) {
	if r == nil {
		return false, io.ErrUnexpectedEOF
	}

	if len(seq) == 0 || seq == nil {
		return false, errors.New("Нет последовательности для поиска")
	}

	buf := make([]byte, 1024)
	var result []byte

	for {
		num, err := r.Read(buf)
		if err != nil {
			if err == io.EOF {
				break
			}
			return false, err
		}

		result = append(result, buf[:num]...)

		if bytes.Index(result, seq) != -1 {
			return true, nil
		}

		// Проверка на переполнение
		if len(result) > len(seq) {
			result = result[len(result)-len(seq):]
		}
	}

	return false, nil
}
