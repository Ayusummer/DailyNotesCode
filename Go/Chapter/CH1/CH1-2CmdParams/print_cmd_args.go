package main

import (
	"fmt"
	"os"
	"strings"
)

// 类似于 echo, 默认分隔符为一个空格
func Print_cmd_args() {
	fmt.Println("echo 基本写法:")
	// 定义一个字符串切片, 用于存储命令行参数
	var getParams string
	// 分隔符为一个空格
	var sep string = " "
	// 第 0 个参数是程序名, 第 1 个参数才是实际传入的首个参数
	for i := 1; i < len(os.Args); i++ {
		getParams += os.Args[i] + sep
	}
	fmt.Println(getParams)
}

// 使用切片构造 echo 语句
func Echo_Slice() {
	fmt.Println("echo 切片写法:")
	var getParams, sep string
	sep = " "
	for _, arg := range os.Args[1:] {
		getParams += arg + sep
	}
	fmt.Println(getParams)
}

// 使用 strings.Join() 方法构造 echo 语句
func Echo_Join() {
	fmt.Println("echo strings.Join() 写法:")
	fmt.Println(strings.Join(os.Args[1:], " "))
}

// 不考虑输出格式, 直接打印 os.Args 切片
func Echo_direct_print_slice() {
	fmt.Println("echo 直接打印切片:")
	fmt.Println(os.Args[1:])
}

func main() {
	Print_cmd_args()
	Echo_Slice()
	Echo_Join()
	Echo_direct_print_slice()
}
