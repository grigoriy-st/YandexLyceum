package main

import (
	"fmt"
	"math/rand"
	"time"
)

type User struct {
	ID    int
	Name  string
	Email string
	Age   int
}

type Report struct {
	ReportID int
	Date     string
	User
}

func CreateReport(user User, reportDate string) Report {
	rand.Seed(time.Now().UnixNano())
	randID := rand.Intn(1000)
	return Report{ReportID: randID, Date: reportDate, User: user}
}

func PrintReport(report Report) {
	user := report.User
	fmt.Println(user.ID, user.Name, user.Email, user.Age, report.Date)
}

func GenerateUserReports(users []User, reportDate string) []Report {
	res := []Report{}
	for _, usr := range users {
		res = append(res, CreateReport(usr, reportDate))
	}
	return res
}

func main() {
	user := User{ID: 1, Name: "Иван", Email: "ivan@example.com", Age: 30}
	reportDate := time.Now().Format("2006-01-02")

	report := CreateReport(user, reportDate)

	if report.ID != user.ID {
		fmt.Errorf("Ожидается ID пользователя %d, получено %d", user.ID, report.ID)
	}
	if report.Name != user.Name {
		fmt.Errorf("Ожидается имя пользователя %s, получено %s", user.Name, report.Name)
	}
	if report.Email != user.Email {
		fmt.Errorf("Ожидается Email пользователя %s, получено %s", user.Email, report.Email)
	}
	if report.Age != user.Age {
		fmt.Errorf("Ожидается возраст пользователя %d, получено %d", user.Age, report.Age)
	}

}
