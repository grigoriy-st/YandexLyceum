package main

import (
	"os"
)

func ModifyFile(filename string, pos int, val string) {
	file, err := os.OpenFile(filename, os.O_WRONLY, 0644)
	if err != nil {
		return
	}
	defer file.Close()

	_, _ = file.Seek(int64(pos), 0)
	_, _ = file.WriteString(val)
}

func main() {
	ModifyFile("third.txt", 10, "")
}
