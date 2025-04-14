package main

import (
	"errors"
	"fmt"
	"os"
	"unicode"
)

func IsNum(arg string) bool {
	for _, let := range arg {
		if !unicode.IsDigit(let) {
			return false
		}
	}
	return true
}

func run() error {
	args := os.Args
	if len(args) != 4 {
		return errors.New("Передано большое кол-во аргументов")
	}
	Width := args[1]
	Height := args[2]
	Percent := args[3]

	if !IsNum(Width) || !IsNum(Height) || !IsNum(Percent) {
		return errors.New("Все аргументы должны быть числовыми")
	}

	res := fmt.Sprintf("%sx%s %s%%", Width, Height, Percent)
	err := os.WriteFile("config.txt", []byte(res), 0644)
	if err != nil {
		return errors.New("Ошибка записи")
	}

	return nil
}
func main() {
	run()
}
