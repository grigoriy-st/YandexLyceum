package main

import "fmt"

type User struct {
	Name   string
	Age    int
	Active bool
}

func NewUser(name string, age int, active bool) (*User, error) {
	if name == "" {
		return nil, fmt.Errorf("Параметр Name  обязателен к заполнению: ")
	}
	if age <= 0 {
		age = 18
	}
	if active == false {
		active = true
	}
	return &User{Name: name, Age: age, Active: active}, nil
}

func main() {
	usr1, _ := NewUser("Grigoriy", -1, false)
	fmt.Print(usr1.Name, usr1.Age, usr1.Active)
}
