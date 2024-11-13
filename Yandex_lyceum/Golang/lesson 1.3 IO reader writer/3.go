package main

import "strings"

type UpperWriter struct {
	UpperString string
}

func (uw *UpperWriter) Write(s []byte) (int, error) {
	res := strings.ToUpper(string(s))
	uw.UpperString = res

	return len(s), nil
}
