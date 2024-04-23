package main

import "fmt"

// 编写一个rotate函数，通过一次循环完成旋转 slice 中的所有元素。
func rotate(s []int, n int) []int {
	for i := 0; i < n; i++ {
		s = append(s, s[i])
	}
	return s[n:]
}

func main() {
	var a = []int{0, 1, 2, 3, 4, 5}
	fmt.Printf("旋转前：%v\n", a)
	a = rotate(a, 2)
	fmt.Printf("旋转 2 位后：%v\n", a)
}
