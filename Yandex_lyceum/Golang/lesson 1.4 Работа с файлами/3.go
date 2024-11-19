package main

import (
	"io"
	"os"
)

func CopyFilePart(inputFilename, outFileName string, startpos int) error {
	file, err := os.Open(inputFilename)
	if err != nil {
		return err
	}
	defer file.Close()

	out, err := os.Create(outFileName)
	if err != nil {
		return err
	}
	defer out.Close()

	file_size, _ := file.Stat()
	if startpos > int(file_size.Size()) {
		return nil
	}
	_, err = file.Seek(int64(startpos), io.SeekStart)
	if err != nil {
		return nil
	}

	_, err = io.Copy(out, file)
	return err

}

func main() {
	fileName := "second.txt"
	CopyFilePart(fileName, "out.txt", 20)
}
