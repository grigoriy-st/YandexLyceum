package main

import (
	"fmt"
	"sort"
)

func SortNums(nums []uint) {
	sort.Slice(nums, func(i, j int) bool {
		return nums[i] < nums[j]
	})
}

func main() {
	nums := []uint{3, 5, 1, 0, 2, 10, 4}
	SortNums(nums)

	fmt.Print(nums)
}
