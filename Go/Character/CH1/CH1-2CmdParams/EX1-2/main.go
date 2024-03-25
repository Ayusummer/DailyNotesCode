// 练习 1.2: 修改 echo 程序, 使其打印每个参数的索引和值, 每个一行
package main

import (
	"fmt"
	"os"
)

func echo_ex_1_2() {
	for i, arg := range os.Args[1:] {
		fmt.Println("参数索引:", i, "\t参数值:", arg)
	}
}

func main() {
	echo_ex_1_2()
}
