package main

import "io"

func WriteString(s string, w io.Writer) error {
	_, err := w.Write([]byte(s))
	return err
}

func main() {
	return
}
