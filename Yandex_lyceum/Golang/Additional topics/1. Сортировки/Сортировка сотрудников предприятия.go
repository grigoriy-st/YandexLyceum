package main

import (
	"errors"
	"fmt"
	"sort"
)

type CompanyInterface interface {
	AddWorkerInfo(name, position string, salary, experience uint) error
	SortWorkers() ([]string, error)
}

type Worker struct {
	Name       string
	Position   string
	Salary     uint
	Experience uint
}

type Company struct {
	Workers []Worker
}

func (c *Company) AddWorkerInfo(name, position string, salary, experience uint) error {
	if name == "" || position == "" {
		return errors.New("Incorrect data about worker")
	}
	data := Worker{
		Name:       name,
		Position:   position,
		Salary:     salary,
		Experience: experience,
	}
	c.Workers = append(c.Workers, data)

	return nil
}

func (c *Company) SortWorkers() ([]string, error) {
	if len(c.Workers) == 0 {
		return nil, errors.New("Workers list is empty")
	}

	positionOrder := map[string]int{
		"директор":         1,
		"зам. директора":   2,
		"начальник цеха":  3,
		"мастер":         4,
		"рабочий":        5,
	}

	sort.Slice(c.Workers, func(i, j int) bool {
		first := c.Workers[i].Salary * c.Workers[i].Experience
		second := c.Workers[j].Salary * c.Workers[j].Experience

		if first != second {
			return first > second
		}

		return positionOrder[c.Workers[i].Position] < positionOrder[c.Workers[j].Position]
	})

	var result []string

	for _, worker := range c.Workers {
		income := worker.Salary * worker.Experience
		result = append(result, fmt.Sprintf("%s - %d - %s", worker.Name, income, worker.Position))
	}
	return result, nil
}

func main() {
	company := &Company{}

	// Добавляем сотрудников
	company.AddWorkerInfo("Михаил", "директор", 12000, 12)
	company.AddWorkerInfo("Андрей", "мастер", 9800, 12)
	company.AddWorkerInfo("Игорь", "зам. директора", 11000, 10)
	company.AddWorkerInfo("Светлана", "рабочий", 5000, 6)

	// Сортируем сотрудников и выводим результат
	sortedWorkers, err := company.SortWorkers()
	if err != nil {
		fmt.Println("Ошибка:", err)
		return
	}

	fmt.Println("Отсортированные сотрудники:")
	for _, worker := range sortedWorkers {
		fmt.Println(worker)
	}
}
