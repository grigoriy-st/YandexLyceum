package main

type User struct {
	Name   string
	Age    int
	Active bool
}

func NewUser(name string, params ...interface{}) *User {
	age := 18
	active := true

	for _, el := range params {
		switch v := el.(type) {
		case int:
			if v > 0 {
				age = v
			}
		case bool:
			active = v
		}
	}
	return &User{Name: name, Age: age, Active: active}
}
