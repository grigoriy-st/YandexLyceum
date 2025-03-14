package main

import (
	"fmt"
	"sort"
)

func SortNames(names []string) {
	sort.Slice(names, func(i, j int) bool {
		return names[i] < names[j]
	})
}
func main() {
	names := []string{"Есения", "Арина", "Аксинья", "Варвара"}	
	SortNames(names)
	fmt.Print(names)
}
