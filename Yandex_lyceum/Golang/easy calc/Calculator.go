package main

import (
	"fmt"
	"strconv"
	"strings"
)

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
	lenghtSeq := len(seq)

	for i := 1; i < lenghtSeq; i++ {
		if strings.Contains("*/+-", prevSign) && strings.Contains("*/+-", string(seq[i])) {
			return false, fmt.Errorf("There are two operators in a row")
		}
		if strings.Contains("1234567890.", prevSign) && strings.Contains("1234567890.", string(seq[i])) {
			return false, fmt.Errorf("There are two operands in a row")
		}
		prevSign = string(seq[i])
	}
	if strings.Contains("*/+-", string(seq[lenghtSeq-1])) {
		return false, fmt.Errorf("Operation without operand")
	}
	return true, nil
}

func SolveExpInBrackets(first string, second string, op string) (string, error) {
	firstOperand, _ := strconv.ParseFloat(first, 64)
	secondOperand, _ := strconv.ParseFloat(second, 64)
	tempQ := 0.0

	switch op {
	case "*":
		tempQ = firstOperand * secondOperand
	case "/":
		if secondOperand == 0 {
			return "", fmt.Errorf("Devision by zero")
		}
		tempQ = firstOperand / secondOperand
	case "-":
		tempQ = firstOperand - secondOperand
	case "+":
		tempQ = firstOperand + secondOperand
	}
	out := strconv.FormatFloat(tempQ, 'f', -1, 64)
	return out, nil
}

func IsExpContainBrackets(exp []string) bool {
	for i := 0; i < len(exp); i++ {
		if string(exp[i]) == ")" || string(exp[i]) == "(" {
			return true
		}
	}
	return false
}

func SolveExpression(seq []string) (float64, error) {
	for {
		if len(seq) == 1 {
			break
		}
		if IsExpContainBrackets(seq) {
			length_seq := len(seq)
			indexLeftBracket := -1
			indexRightBracket := -1

			for i := 0; i < length_seq; i++ {
				if string(seq[i]) == "(" {
					if indexLeftBracket == -1 || indexRightBracket == -1 {
						indexLeftBracket = i
					}
				} else if string(seq[i]) == ")" {
					if indexLeftBracket != -1 || indexRightBracket == -1 {
						indexRightBracket = i
						break
					}
				}
			}

			resultExp, err := SolveExpInBrackets(seq[indexLeftBracket+1],
				seq[indexLeftBracket-1],
				seq[indexLeftBracket])
			if err != nil {
				return 0.0, fmt.Errorf(err.Error())
			}
			tempExpression := seq[:indexLeftBracket]
			tempExpression = append(tempExpression, resultExp)

			for _, val := range seq[indexRightBracket+1:] { // Добавление оставшейся части выражения
				tempExpression = append(tempExpression, string(val))
			}
			seq = tempExpression
		} else {
			break
		}

	}
	result, _ := strconv.ParseFloat(string(seq[0]), 64)
	return result, nil
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
