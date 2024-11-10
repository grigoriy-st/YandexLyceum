package main

import (
	"fmt"
	"reflect"
)

type Vehicle interface {
	CalculateTravelTime(distance float64) float64
	GetType() string
}

type Car struct {
	Speed    float64
	Type     string
	FuelType string
}

func (c Car) CalculateTravelTime(distance float64) float64 {
	return distance / c.Speed
}

func (c Car) GetType() string {
	return reflect.TypeOf(c).String()
}

type Motorcycle struct {
	Speed    float64
	Type     string
	FuelType string
}

func (m Motorcycle) CalculateTravelTime(distance float64) float64 {
	return distance / m.Speed
}

func (m Motorcycle) GetType() string {
	return reflect.TypeOf(m).String()
}

func EstimateTravelTime(vehicles []Vehicle, distance float64) map[string]float64 {
	res_map := make(map[string]float64)

	for _, v := range vehicles {
		res_map[v.GetType()] = v.CalculateTravelTime(distance)
	}

	return res_map
}

func main() {
	car := Car{Type: "Седан", Speed: 60.0, FuelType: "Бензин"}
	motorcycle := Motorcycle{Type: "Мотоцикл", Speed: 80.0}
	car2 := Car{Type: "Чурка", Speed: 60.0, FuelType: "Бензин"}
	vehicles := []Vehicle{car, car2, motorcycle}

	distance := 200.0

	travelTimes := EstimateTravelTime(vehicles, distance)

	expectedCarTime := distance / car.Speed
	fmt.Print(travelTimes["main.Car"])
	if travelTimes["main.Car"] != expectedCarTime {
		fmt.Errorf("Ожидается время для автомобиля %.2f часа, получено %.2f", expectedCarTime, travelTimes["main.Car"])
	}

	expectedMotorcycleTime := distance / motorcycle.Speed
	if travelTimes["main.Motorcycle"] != expectedMotorcycleTime {
		fmt.Errorf("Ожидается время для мотоцикла %.2f часа, получено %.2f", expectedMotorcycleTime, travelTimes["main.Motorcycle"])
	}
}
