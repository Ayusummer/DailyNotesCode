// 练习 1.1： 修改 echo 程序，使其能够打印 os.Args[0]，即被执行命令本身的名字。
package main

import (
	"fmt"
	"os"
)

func echo_ex_1_1() {
	fmt.Println("执行命令本身的名字:", os.Args[0])
	fmt.Println("命令行参数:", os.Args[1:])
}

func main() {
	echo_ex_1_1()
}
