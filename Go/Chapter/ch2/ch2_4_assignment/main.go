package main

import "fmt"

func assign() {
	// 定义一个 map 字典
	var m map[string]int = map[string]int{"one": 1, "two": 2, "three": 3}
	// 尝试读取一个 m 中存在的 key
	v, ok := m["one"]
	ok1_2 := m["one"]
	println(v, ok)
	println(ok1_2)
	// 尝试读取一个 m 中不存在的 key
	v2, ok2 := m["four"]
	ok2_2 := m["four"]
	// 打印结果
	println(v2, ok2)
	println(ok2_2)
}

func compare() {
	type Celsius float64
	type Fahrenheit float64
	c := Celsius(100)
	f := Fahrenheit(212)

	// 可以将 Fahrenheit 赋值给 Celsius 类型，因此可以进行相等比较
	fmt.Println(c == Celsius(f)) // 输出: true

	// 可以将 Celsius 赋值给 Fahrenheit 类型，因此可以进行相等比较
	fmt.Println(f == Fahrenheit(c)) // 输出: true
}

func main() {
	compare()
}
