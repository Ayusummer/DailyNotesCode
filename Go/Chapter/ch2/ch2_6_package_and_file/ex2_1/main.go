package main

import (
	// "CH2_6/tempconv"
	"GoLearning/Chapter/ch2/ch2_6_package_and_file/ex2_1/tempconv"
	"fmt"
)

func main() {
	c1 := tempconv.Celsius(100)
	f1 := tempconv.CToF(c1)
	fmt.Println("100°C to Fahrenheit:", f1)
	k1 := tempconv.CToK(c1)
	fmt.Println("100°C to Kelvin:", k1)
}
