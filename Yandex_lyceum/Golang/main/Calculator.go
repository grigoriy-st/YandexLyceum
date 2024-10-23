package main

import (
	"fmt"
	"strconv"
	"strings"
)

func ExecuteBinOps(seq []string, pos int, sign string) ([]string, error) {
	// выполняет все арифметические операции
	first, _ := strconv.ParseFloat(seq[pos-1], 64)
	second, _ := strconv.ParseFloat(seq[pos+1], 64)
	tempQ := 0.0

	switch sign {
	case "*":
		tempQ = first * second
	case "/":
		if second == 0 {
			return []string{}, fmt.Errorf("Devision by zero")
		}
		tempQ = first / second
	case "-":
		tempQ = first - second
	case "+":
		tempQ = first + second
	}
	//
	out := seq[:pos-1]
	resBinExp := strconv.FormatFloat(tempQ, 'f', -1, 64)
	out = append(out, resBinExp) // result BinExp

	for _, val := range seq[pos+2:] { // PartAfterExp
		out = append(out, string(val))
	}
	return out, nil
}

func ExecuteArifOps(seq []string) (string, error) {
	for {
		if len(seq) == 1 {
			break
		}

		// Выполнение приоритетных операций
		for i := 0; i < len(seq); i++ {
			if string(seq[i]) == "*" || string(seq[i]) == "/" {
				tempSeq, err := ExecuteBinOps(seq, i, string(seq[i])) // seq, индекс операции, операция
				if err != nil {
					return "", fmt.Errorf(err.Error())
				}
				seq = tempSeq
			}
		}

		// Выполнение других операций
		for i := 0; i < len(seq); i++ {
			if string(seq[i]) == "+" || string(seq[i]) == "-" {
				tempSeq, err := ExecuteBinOps(seq, i, string(seq[i]))
				if err != nil {
					return "", fmt.Errorf(err.Error())
				}
				seq = tempSeq
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
			indexLeftBracket := -1
			indexRightBracket := -1

			for i := 0; i < length_seq; i++ {
				if string(exp[i]) == "(" {
					if indexLeftBracket == -1 || indexRightBracket == -1 {
						indexLeftBracket = i
					}
				} else if string(exp[i]) == ")" {
					if indexLeftBracket != -1 || indexRightBracket == -1 {
						indexRightBracket = i
						break
					}
				}
			}
			tempExp := exp[indexLeftBracket+1 : indexRightBracket] // передача выражения вместе со скобками
			resultExp, err := ExecuteArifOps(tempExp)
			if err != nil {
				return 0.0, nil
			}
			tempExpression := exp[:indexLeftBracket]
			tempExpression = append(tempExpression, resultExp)

			for _, val := range exp[indexRightBracket+1:] { // Добавление оставшейся части выражения
				tempExpression = append(tempExpression, string(val))
			}
			exp = tempExpression
		} else {
			break
		}

	}
	tempExp, err := ExecuteArifOps(exp)
	if err != nil {
		return 0.0, fmt.Errorf(err.Error())
	}
	result, _ := strconv.ParseFloat(tempExp, 64)
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

	result, err := SolveExpression(parts)
	if err != nil {
		return 0.0, fmt.Errorf(err.Error())
	}

	return result, nil
}

func main() {
	d := "1+1" // 2
	// d := "(2+2)*2" // 8
	// d := "2+2*2" // 6
	// d := "1/2" // 0.5
	fmt.Println(Calc(d))
}
