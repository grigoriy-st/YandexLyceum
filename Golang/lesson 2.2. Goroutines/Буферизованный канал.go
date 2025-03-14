package main

const capacity = 10

func Process(nums []int) chan int {
	ch := make(chan int, capacity)

	for num := range nums {
		ch <- num
	}

	return ch
}

func main() {
	Process([]int{1, 2, 3, 4})
}
