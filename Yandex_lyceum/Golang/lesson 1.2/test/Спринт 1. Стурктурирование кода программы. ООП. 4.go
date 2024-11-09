package main

type Vehicle interface {
	CalculateTravelTime(distance float64) float64
	GetType() string
}

func (c Car) CalculateTravelTime(distance float64) float64 {
	return distance / c.Speed
}

type Car struct {
	Speed    float64
	Type     string
	FuelType string
}

func (c Car) GetType() string {
	return c.Type
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
	return m.Type
}

func EstimateTravelTime(vehicle []Vehicle, distance float64) map[string]float64 {
	res_map := make(map[string]float64)

	for _, v := range vehicle {
		res_map[v.GetType()] = v.CalculateTravelTime(distance)
	}

	return res_map
}

func main() {
	car := Car{Type: "Седан", Speed: 60.0, FuelType: "Бензин"}
	motorcycle := Motorcycle{Type: "Мотоцикл", Speed: 80.0}

	vehicles := []Vehicle{car, motorcycle}

	distance := 200.0

	travelTimes := EstimateTravelTime(vehicles, distance)

	expectedCarTime := distance / car.Speed
	if travelTimes["main.Car"] != expectedCarTime {
		t.Errorf("Ожидается время для автомобиля %.2f часа, получено %.2f", expectedCarTime, travelTimes["main.Car"])
	}

	expectedMotorcycleTime := distance / motorcycle.Speed
	if travelTimes["main.Motorcycle"] != expectedMotorcycleTime {
		t.Errorf("Ожидается время для мотоцикла %.2f часа, получено %.2f", expectedMotorcycleTime, travelTimes["main.Motorcycle"])
	}
}
