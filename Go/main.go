package main

import (
	"GoLearning/pkg/cmd_param"
	"fmt"
)

func main() {
	fmt.Println("echo 基本写法:")
	cmd_param.Print_cmd_args()
	fmt.Println("echo 切片写法:")
	cmd_param.Echo_Slice()
	fmt.Println("echo strings.Join() 写法:")
	cmd_param.Echo_Join()
	fmt.Println("echo 直接打印切片:")
	cmd_param.Echo_direct_print_slice()
}
