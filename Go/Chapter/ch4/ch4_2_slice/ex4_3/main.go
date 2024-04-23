// 重写reverse函数，使用数组指针代替slice。
package main

import "fmt"

// 重写reverse函数，使用数组指针代替slice。
func reverse(s *[]int) {
	for i, j := 0, len(*s)-1; i < j; i, j = i+1, j-1 {
		(*s)[i], (*s)[j] = (*s)[j], (*s)[i]
	}
}

func main() {
	var a = []int{0, 1, 2, 3, 4, 5}
	reverse(&a)
	fmt.Println(a)
}
