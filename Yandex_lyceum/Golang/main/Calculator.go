package main

import (
	"fmt"
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
				i -= 1
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

func IsExpContainBrackets(exp []string) bool {
	for i := 0; i < len(exp); i++ {
		if string(exp[i]) == ")" || string(exp[i]) == "(" {
			return true
		}
	}
	return false
}

func SolveExpression(exp []string) (float64, error) {
	for {
		if len(exp) == 1 {
			break
		}
		if IsExpContainBrackets(exp) {
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
				return 0.0, nil
			}
			TempExpression := exp[:IndexLeftBracket]
			TempExpression = append(TempExpression, ResultExp)

			for _, val := range exp[IndexRightBracket+1:] { // Добавление оставшейся части выражения
				TempExpression = append(TempExpression, string(val))
			}
			exp = TempExpression
		} else {
			break
		}

	}
	TempExp, err := ExecuteArifOps(exp)
	if err != nil {
		fmt.Println(err)
	}
	result, _ := strconv.ParseFloat(TempExp, 64)
	return result, nil
}

func StrToSlice(str string) ([]string, error) {
	result := []string{}
	tempNum := []string{}
	lenghtSeq := len(str)

	for i, value := range str {
		if strings.Contains("+)(-/*", string(value)) {
			if len(tempNum) > 0 {
				num := strings.Join(tempNum, "")
				result = append(result, num)
				tempNum = []string{}
			}
			result = append(result, string(value))
		} else if strings.Contains("1234567890.", string(value)) {
			tempNum = append(tempNum, string(value))

			if i == lenghtSeq-1 {
				num := strings.Join(tempNum, "")
				result = append(result, num)
			}
		} else if string(value) == " " {
			if len(tempNum) > 0 {
				num := strings.Join(tempNum, "")
				result = append(result, num)
				tempNum = []string{}
			}
		} else {
			return []string{}, fmt.Errorf("Invalid sign")
		}
	}

	return result, nil
}

func IsRightSequence(seq []string) (bool, error) {
	prevSign := string(seq[0])
	for i := 1; i < len(seq); i++ {
		if strings.Contains("*/+-", prevSign) && strings.Contains("*/+-", string(seq[i])) {
			return false, fmt.Errorf("There are two operators in a row")
		}
		if strings.Contains("1234567890.", prevSign) && strings.Contains("1234567890.", string(seq[i])) {
			return false, fmt.Errorf("There are two operands in a row")
		}
		prevSign = string(seq[i])
	}
	return true, nil
}

func Calc(expression string) (float64, error) {

	if strings.Contains(expression, ")") {
		if strings.Count(expression, ")") != strings.Count(expression, ")") {
			return 0.0, fmt.Errorf("Different number of brackets")
		}
	}
	parts, err := StrToSlice(expression)
	if err != nil {
		return 0.0, fmt.Errorf(err.Error())
	}

	_, err = IsRightSequence(parts)
	if err != nil {
		return 0.0, fmt.Errorf(err.Error())
	}
	fmt.Println(parts)

	result, err := SolveExpression(parts)
	if err != nil {
		fmt.Println(err)
	}

	return result, nil
}

func main() {
	// a := "4 * (15 * 3 / (10 - 9))"parts = {[]string} len:14, cap:16
	// b := "3 + 5 * (2 - 1) / 4"
	// c := "7.112 + 5 - 3.3 * (10.23 + 5.3 * 4.1) - 1"
	d := "1+3*6-(10*3)+5"
	// e := "3 + * 5"

	fmt.Println(Calc(d))
}
