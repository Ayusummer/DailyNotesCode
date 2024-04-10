package main

import (
	// "CH2_6/tempconv"

	popcount "GoLearning/Chapter/ch2/ch2_6_package_and_file/popcount"
	"fmt"
	"log"
)

var cwd string = "22222222"

func aaaa() string {
	cwd, err := "10", "2"
	// err := "2"
	// cwd = "dtrcfyvgubhinj"
	if err != "2" {
		log.Fatalf("os.Getwd failed: %v", err)
	}
	fmt.Println("Working directory = %s", cwd)
	fmt.Printf("内部:")
	fmt.Println(&cwd)
	return cwd
}

func main() {
	// fmt.Printf("外部:")
	// fmt.Println(&cwd)
	// // c1 := tempconv.Celsius(100)
	// // f1 := tempconv.CToF(c1)
	// // fmt.Println("100°C to Fahrenheit:", f1)
	// // k1 := tempconv.CToK(c1)
	// // fmt.Println("100°C to Kelvin:", k1)
	// cwd = aaaa()
	// fmt.Print("dwqefweqwd" + cwd)
	popcount.PopCount(0x1234567890ABCDEF)
}
