package main

import (
	"fmt"
	"math/cmplx"
)

// 基础复数示例
func baseComplex() {
	var x complex128 = complex(1, 2) // 1+2i
	var y complex128 = complex(3, 4) // 3+4i
	fmt.Println(x * y)               // "(-5+10i)"
	fmt.Println(real(x * y))         // "-5"
	fmt.Println(imag(x * y))         // "10"

}

// 复数运算
func complexOperation() {
	fmt.Println(1i * 1i) // "(-1+0i)", i^2 = -1
}

// 简化复数声明
func simpleComplex() {
	x := 1 + 2i
	y := 3 + 4i
	fmt.Println(x * y) // "(-5+10i)"
}

// math/cmplx包提供了复数的标准库
func complexMath() {
	fmt.Println(cmplx.Abs(3 + 4i)) // "5"
	fmt.Println(cmplx.Sqrt(-1))    // "(0+1i)"
}

func main() {
	// baseComplex()
	// complexOperation()
	// simpleComplex()
	complexMath()
}
