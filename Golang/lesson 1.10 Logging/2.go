package main

import (
	"log"
)

type OrderLogger struct {
}

func NewOrderLogger() *OrderLogger {
	return &OrderLogger{}
}

type Order struct {
	OrderNumber  int
	CustomerName string
	OrderAmount  float64
}

func (logger *OrderLogger) AddOrder(order Order) {
	log.Printf("Добавлен заказ #%d, Имя клиента: %s, Сумма заказа: $%.2f", order.OrderNumber, order.CustomerName, order.OrderAmount)
}
