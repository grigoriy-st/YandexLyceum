package main

import (
	"fmt"
	"math"
)

type Circle struct {
	radius float64
}

func (c *Circle) Aria() float64 {
	return math.Pi * c.radius * c.radius
}

func NewCircle(radius float64) *Circle {
	return &Circle{radius: radius}
}

func main() {
	f := NewCircle(3.15)
	fmt.Print(f.Aria())
}
