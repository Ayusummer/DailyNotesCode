package main

import "fmt"

func main() {
	var map_a = map[string]int{
		"one": 1,
	}

	fmt.Printf("map_a[\"one\"]: %d\n", map_a["on"]) // map_a["one"]: 1

}
