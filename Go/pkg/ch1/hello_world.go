package ch1

import "fmt"

func Printch1World() {
	fmt.Println("Hello World")
	// 获取用户输出, 防止程序退出
	var input string
	fmt.Scanln(&input)
}
