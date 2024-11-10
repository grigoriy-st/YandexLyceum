package main

import "errors"

type Account struct {
	balance float64
	owner   string
}

func NewAccount(name string, acc_balace ...float64) Account {
	balance := 0.0
	if len(acc_balace) > 0 {
		balance = acc_balace[0]
	}
	return Account{balance: balance, owner: name}
}

func (a *Account) SetBalance(new_balance float64) error {
	if new_balance > 0 {
		a.balance = new_balance
	} else {
		return errors.New("Передано отрицательное число")
	}
	return nil
}

func (a Account) GetBalance() float64 {
	return a.balance
}

func (a *Account) Deposit(money float64) error {
	if money > 0 {
		a.balance += money
	} else {
		return errors.New("Передано отрицательное число")
	}
	return nil
}

func (a *Account) Withdraw(money float64) error {
	if money > 0 && a.balance-money >= 0 {
		a.balance = a.balance - money
	} else {
		return errors.New("Передано отрицательное число")
	}
	return nil
}

func main() {
	account := NewAccount("Alice")

	// Устанавливаем баланс
	err := account.SetBalance(1000.0)
	if err != nil {
		t.Errorf("Ошибка при установке баланса: %v", err)
	}

	// Вносим деньги
	err = account.Deposit(500.0)
	if err != nil {
		t.Errorf("Ошибка при внесении денег: %v", err)
	}

	// Снимаем деньги
	err = account.Withdraw(200.0)
	if err != nil {
		t.Errorf("Ошибка при снятии денег: %v", err)
	}

	// Получаем текущий баланс
	balance := account.GetBalance()
	expectedBalance := 1300.0
	if balance != expectedBalance {
		t.Errorf("Ожидается баланс %.2f, получено %.2f", expectedBalance, balance)
	}
}
