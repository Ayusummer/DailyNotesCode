package main

import "fmt"

type Celsius float64    // 摄氏温度
type Fahrenheit float64 // 华氏温度

const (
	AbsoluteZeroC Celsius = -273.15 // 绝对零度
	FreezingC     Celsius = 0       // 结冰点温度
	BoilingC      Celsius = 100     // 沸水温度
)

func CToF(c Celsius) Fahrenheit { return Fahrenheit(c*9/5 + 32) }

func FToC(f Fahrenheit) Celsius { return Celsius((f - 32) * 5 / 9) }

func compare() {
	var c Celsius
	var f Fahrenheit
	fmt.Println(c == 0) // "true"
	fmt.Println(f >= 0) // "true"
	// fmt.Println(c == f)          // compile error: type mismatch
	fmt.Println(c == Celsius(f)) // "true"!
}

func printTest() {
	c := FToC(212.0)
	// fmt.Println(c.String()) // "100°C"
	fmt.Printf("%v\n", c)   // "100°C"; no need to call String explicitly
	fmt.Printf("%s\n", c)   // "100°C"; 使用 %v 格式化字符串表示, 由于 Celsius 类型已经定义了 String() 方法, 所以会自动调用, 输出为 "100°C"
	fmt.Println(c)          // "100°C"; 使用 %s 格式化字符串表示, 同样会调用 String() 方法, 输出为 "100°C"
	fmt.Printf("%g\n", c)   // "100"; does not call String;使用 %g 格式化字符串表示, 不会调用 String() 方法, 输出为 "100"
	fmt.Println(float64(c)) // "100"; does not call String; 直接打印 Celsius 类型的底层 float64 值, 不会调用 String() 方法, 输出为 "100"
}

func main() {
	// fmt.Printf("%g\n", BoilingC-FreezingC) // "100" °C
	// boilingF := CToF(BoilingC)
	// fmt.Printf("%g\n", boilingF-CToF(FreezingC)) // "180" °F
	// fmt.Printf("%g\n", boilingF-FreezingC)       // compile error: type mismatch

	// compare()

	printTest()
}
