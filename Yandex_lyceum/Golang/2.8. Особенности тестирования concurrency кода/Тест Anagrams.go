package main

import (
	"testing"
)

func TestAreAnagrams(t *testing.T) {
	tests := []struct {
		str1           string
		str2           string
		expectedResult bool
	}{
		{"hello", "olleh", true},
		{"malo", "mrl", false},
		{"first", "tsrif", true},
		{"Listen", "Silent", true},
		{"Dormitory", "Dirty room", false},
		{"The eyes", "They see", true},
		{"", "", true},
		{"a", "a", true},
		{"a", "b", false},
	}

	for _, test := range tests {
		got := AreAnagrams(test.str1, test.str2)
		if got != test.expectedResult {
			t.Errorf("AreAnagrams(%q, %q) = %v; want %v", test.str1, test.str2, got, test.expectedResult)
		}
	}
}
