package main

import (
	"sort"
	"strings"
)

func areScrambled(s1, s2 string) bool {
	if len(s1) != len(s2) {
		return false
	}

	s1Slice := strings.Split(s1, "")
	s2Slice := strings.Split(s2, "")

	sort.Strings(s1Slice)
	sort.Strings(s2Slice)

	return strings.Join(s1Slice, "") == strings.Join(s2Slice, "")
}

func main() {
	var s1 = "abcbefghijk"
	var s2 = "ahijkbcbefg"
	println(areScrambled(s1, s2))
}
