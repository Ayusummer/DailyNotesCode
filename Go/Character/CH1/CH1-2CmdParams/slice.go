package main

import "fmt"

func Slice_test() {
	var a = [3]int{1, 2, 3}
	fmt.Println("a[0]:", a[0], "a[1]:", a[1])
	fmt.Println("a[0:2]:", a[0:2])
}
