package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func ExecuteBinOps(seq []string, pos int, sign string) ([]string, error) {
	// выполняет все арифметические операции выражения в скобках
	first, _ := strconv.ParseFloat(seq[pos-1], 64)
	second, _ := strconv.ParseFloat(seq[pos+1], 64)
	TempQ := 0.0

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

	PartBeforeExp := seq[:pos-1] // rename PartBeforeExp
	ResBinExp := strconv.FormatFloat(TempQ, 'f', -1, 64)
	PartBeforeExp = append(PartBeforeExp, ResBinExp) // result BinExp

	for _, val := range seq[pos+2:] { // PartAfterExp
		PartBeforeExp = append(PartBeforeExp, string(val))
	}
	return PartBeforeExp, nil
}

func ExecuteArifOps(seq []string) (string, error) {
	// ( 10 + 5 * 4 )
	// result := 0

	for {
		if len(seq) == 1 {
			break
		}
		// Execute high priority operations
		for i := 0; i < len(seq); i++ {
			if string(seq[i]) == "*" || string(seq[i]) == "/" {
				TempSeq, err := ExecuteBinOps(seq, i, string(seq[i])) // seq, индекс операции, операция
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
	return seq[0], nil
}

func FindRightBrckt(exp []string, startIndex int) int {
	for i := startIndex; i < len(exp); i++ {
		if string(exp[i]) == ")" {
			return i
		}
	}
	return -1
}

func ProcSlcWithBrckts(exp []string) []string {
	// Функция избавляется и вычисляет все выражения со скобками
	// Возвращает сроку с выражениями без скобок

	for {
		// Выход из циклас помощью нахождения скобок
		if FindRightBrckt(exp, 0) == -1 {
			break
		}

		length_seq := len(exp)
		IndexLeftBracket := -1
		IndexRightBracket := -1

		for i := 0; i < length_seq; i++ {
			if string(exp[i]) == "(" {
				if IndexLeftBracket == -1 || IndexRightBracket == -1 {
					IndexLeftBracket = i
				}
			} else if string(exp[i]) == ")" {
				if IndexLeftBracket != -1 || IndexRightBracket == -1 {
					IndexRightBracket = i
					break
				}
			}
		}
		TempExp := exp[IndexLeftBracket+1 : IndexRightBracket] // передача выражения вместе со скобками
		ResultExp, err := ExecuteArifOps(TempExp)
		if err != nil {
			return []string{}
		}
		TempExpression := exp[:IndexLeftBracket]
		TempExpression = append(TempExpression, ResultExp)

		for _, val := range exp[IndexRightBracket+1:] { // Добавление оставшейся части выражения
			TempExpression = append(TempExpression, string(val))
		}
		exp = TempExpression
	}
	return exp
}

func ProcSlcWithoutBrckts(seq []string) (float64, error) {
	for {
		if len(seq) == 1 {
			break
		}
		for i := 0; i < len(seq); i++ {
			if string(seq[i]) == "*" || string(seq[i]) == "/" {
				TempSeq, err := ExecuteBinOps(seq, i, string(seq[i])) // seq, индекс операции, операция
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
	result, _ := strconv.ParseFloat(seq[0], 64)
	return result, nil
}

func Calc(expression string) (float64, error) {
	RightsBracketsInSeq := false // правильный учёт расположения и наличия скобок

	if (strings.Contains(expression, "(") == strings.Contains(expression, ")")) &&
		strings.Count(expression, "(") >= 1 {
		RightsBracketsInSeq = true
	}
	re := regexp.MustCompile(`(-?\d+\.\d+|-?\d+|\(|\)|\+|-|\*|/)`)
	parts := re.FindAllString(expression, -1)
	fmt.Println(parts)

	if RightsBracketsInSeq {
		parts = ProcSlcWithBrckts(parts)
	}
	result, err := ProcSlcWithoutBrckts(parts)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Print(result)
	return result, nil
}

func main() {
	// a := "4 * (15 * 3 / (10 - 9))"
	// b := "3 + 5 * (2 - 1) / 4"
	c := "7.112 + 5 - 3.3 * (10.23 + 5.3 * 4.1) - 1"
	// d := "1+3*6-(10*3)+5"
	// e := "3 + * 5"

	fmt.Println(Calc(c))
}
