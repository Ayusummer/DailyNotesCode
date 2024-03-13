package main

import (
	"fmt"
)

const boilingF = 212.0

func main_boiling() {
	var f = boilingF
	var c = (f - 32) * 5 / 9
	// %g - general - 根据情况选择十进制或科学计数法进行格式化以提供更紧凑的输出
	fmt.Printf("boiling point = %g°F or %g°C\n", f, c)
	// 输出：
	// boiling point = 212°F or 100°C

}
