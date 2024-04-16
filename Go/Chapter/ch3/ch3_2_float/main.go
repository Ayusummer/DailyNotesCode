package main

import (
	"fmt"
	"math"
)

// float32 精度很有限
func float32Limit() {
	var f float32 = 16777216 // 1 << 24
	fmt.Println(f == f+1)    // "true"!
	fmt.Println(f, f+1)
}

// 控制精度与宽度的浮点数打印
func floatPrint() {
	for x := 0; x < 8; x++ {
		fmt.Printf("x = %d e^x = %8.3f\n", x, math.Exp(float64(x)))
	}
}

// NAN 和 INF
func nanInf() {
	var z float64
	fmt.Println(z, -z, 1/z, -1/z, z/z) // "0 -0 +Inf -Inf NaN"
}

// NAN比较
func nanCompare() {
	nan := math.NaN()
	fmt.Println(nan == nan, nan < nan, nan > nan) // "false false false"
}

func main() {
	// float32Limit()
	// floatPrint()
	// nanInf()
	nanCompare()
}
