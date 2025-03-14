package main

import (
	"fmt"
	"time"
)

func QuizRunner(questions, answers []string, answerCh chan string) int {
	correctAnswers := 0

	for i, _ := range questions {

		select {
		case userAnswer := <-answerCh:
			if userAnswer == answers[i] {
				correctAnswers++
			}
		case <-time.After(1 * time.Second):
			continue
		}
	}

	return correctAnswers
}

func main() {
	questions := []string{
		"What is the capital of France?",
		"Who wrote \"Romeo and Juliet\"?",
		"What is the largest planet in our solar system?",
		"How many continents are there on Earth?",
		"What is the chemical symbol for water?",
	}
	answers := []string{"Paris", "William Shakespeare", "Jupiter", "Seven", "H2O"}
	answerCh := make(chan string)

	fmt.Println(QuizRunner(questions, answers, answerCh))

}
