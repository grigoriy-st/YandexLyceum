package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func ExecuteBinOps(seq []string, pos int, sign string) ([]string, error) {
	first, _ := strconv.Atoi(seq[pos-1])
	second, _ := strconv.Atoi(seq[pos+1])
	TempQ := 0

	switch sign {
	case "*":
		TempQ = first * second
	case "/":
		if second == 0 {
			return []string{}, fmt.Errorf("Devision by zero")
		}
		TempQ = first / second
	case "-":
		TempQ = first - second
	case "+":
		TempQ = first + second
	}

	TempSeq := seq[:pos-1]
	TempQStr := strconv.Itoa(TempQ)
	TempSeq = append(seq, TempQStr)

	for _, val := range seq[pos+2:] {
		TempSeq = append(TempSeq, string(val))
	}
	return seq, nil
}

func ExecuteArifOps(seq []string) (int, error) {
	// 10 + 5 * 4
	result := 0

	for {
		if len(seq) == 1 {
			break
		}
		// Execute high priority operations
		for i := 0; i < len(seq); i++ {
			if string(seq[i]) == "*" || string(seq[i]) == "/" {
				TempSeq, err := ExecuteBinOps(seq, i, string(seq[i]))
				if err != nil {
					fmt.Println(err)
				}
				seq = TempSeq
			}
		}
		// Execute other operations
		for i := 0; i < len(seq); i++ {
			if string(seq[i]) == "+" || string(seq[i]) == "-" {
				TempSeq, err := ExecuteBinOps(seq, i, string(seq[i]))
				if err != nil {
					fmt.Println(err)
				}
				seq = TempSeq
			}
		}
	}
	return -1
}

func FindRightBrckt(exp []string, startIndex int) int {
	for i := startIndex; i < len(exp); i++ {
		if string(exp[i]) == ")" {
			return i
		}
	}
	return -1
}

func FindLeftBrckt(exp []string, startIndex int) int {
	for i := startIndex; i >= 0; i-- {
		if string(exp[i]) == "(" {
			return i
		}
	}
	return -1
}

func ProcSlcWthBrckts(exp []string) []string {
	for {
		length_seq := len(exp)
		var half_lenght int = length_seq / 2

		IndexLeftBracket := -1
		IndexRightBracket := -1

		for i := 0; i < length_seq; i++ {
			if string(exp[i]) == "(" {
				if IndexLeftBracket == -1 || IndexRightBracket == -1 {
					IndexLeftBracket = i
				}
			}
			if string(exp[i]) == ")" {
				if IndexLeftBracket != -1 || IndexRightBracket == -1 {
					IndexRightBracket = i
					break
				}
			}
		}
		TempExp := exp[IndexLeftBracket : IndexRightBracket+1]
		ResultTempExp := ExecuteArifOps(TempExp)

	}
	return nil
}

func Calc(expression string) (float64, error) {
	RightsBracketsInSeq := false // правильный учёт расположения и наличия скобок

	if (strings.Contains(expression, "(") == strings.Contains(expression, ")")) &&
		strings.Count(expression, "(") > 1 {
		RightsBracketsInSeq = true
	}
	re := regexp.MustCompile(`\d+|[+\-*\/()]`)
	parts := re.FindAllString(expression, -1)

	if RightsBracketsInSeq {
		parts = ProcSlcWthBrckts(parts)
	}
	fmt.Println(parts)
	// sequensly solving
	return 0.0, nil
}

func main() {
	a := "4 * (15 * 3 / (10 - 9))"
	// b := "3 + 5 * (2 - 1) / 4"
	// c := "7 + 5 - 3 * (10 + 5 * 4) - 1"
	// d := "1+3*6-(10*3)+5"
	// e := "3 + * 5"

	fmt.Println(Calc(a))
}
