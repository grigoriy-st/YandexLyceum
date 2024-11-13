package main

import "io"

func Copy(r io.Reader, w io.Writer, n uint) error {
	if n == 0 {
		return nil
	}

	copiedBytes := uint(0)
	buf := make([]byte, 1024)
	for copiedBytes < n {
		lenBytesToRead := int(n - copiedBytes)
		if lenBytesToRead > len(buf) {
			lenBytesToRead = len(buf)
		}

		bytesRead, err := r.Read(buf[:lenBytesToRead])

		if err != nil {
			if err == io.EOF {
				break
			}
			return err
		}

		if bytesRead == 0 {
			break
		}

		bytesWritten, err := w.Write(buf[:bytesRead])

		if err != nil {
			return err
		}
		copiedBytes += uint(bytesWritten)
	}
	return nil
}
