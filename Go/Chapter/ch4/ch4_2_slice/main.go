package main

import "fmt"

// reverse reverses a slice of ints in place.
func reverse(s []int) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

func slice_append_sample() {
	var runes []rune
	for _, r := range "Hello, 世界" {
		runes = append(runes, r)
	}
	fmt.Printf("%q\n", runes) // "['H' 'e' 'l' 'l' 'o' ',' ' ' '世' '界']"
}

func main() {
	var a = make([]int, 5) // len(a)=5
	var cap_a = cap(a)
	fmt.Printf("cap_a: %d\n", cap_a)
	var b = []int{0, 1, 2, 3, 4, 5, 7, 8, 9, 10}
	var cap_b = cap(b)
	fmt.Printf("cap_b: %d\n", cap_b)

	reverse(a[:2]) // a = [1, 0, 2, 3, 4, 5]
	fmt.Println(a)
	slice_append_sample()
}
