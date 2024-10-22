package main

import (
	"fmt"
	"regexp"
	"strconv"
)

func find_elment(seq []string, el string) int {
	for i, val := range seq {
		if val == el {
			return i
		}
	}
	return -1
}

func CalcExp(exp string) string {
	//result := 0
	re := regexp.MustCompile(`\d+|[+\-*\/()]`)
	parts := re.FindAllString(exp, -1)

	for {
		temp_num := 0
		index := find_elment(parts, "*")
		if index != -1 {
			first, _ := strconv.Atoi(parts[index-1])
			second, _ := strconv.Atoi(parts[index+1])
			temp_num = first * second
			temp_str := strconv.Itoa(temp_num)

			temp_parts := parts[:index-1]
			temp_parts = append(temp_parts, temp_str)
			for _, val := range parts[index+2:] {
				temp_parts = append(temp_parts, val)
			}
			parts = temp_parts
		}
	}
	return "e"
}

func Calc(expression string) (float64, error) {
	// find ( and ), and solve those expressions
	// if string.Count
	// cur_str := expression

	first_index := 0
	second_index := 0
	for i, l_val := range expression {

		if l_val == '(' {
			first_index = i

			for j, r_val := range expression {
				if r_val == ')' {
					second_index = j

					solve_exp := CalcExp(expression[first_index-1 : second_index])
					expression = expression[:first_index] + solve_exp + expression[second_index+1:]
					fmt.Println(expression)
				}
			}
		}
	}
	// sequensly solving
	return 0.0, nil
}

func main() {
	fmt.Println(Calc("1+3*6-(10*3)+5"))

}
