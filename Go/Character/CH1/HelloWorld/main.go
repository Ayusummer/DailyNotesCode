package main

import "fmt"

func main() {
	fmt.Println("Hello, World!")
	// 获取用户输入, 防止程序自动退出
	var input string
	fmt.Scanln(&input)
}
