package main

import(
	"fmt"
	"os"
)

func main(){
	// 向同级目录写一个 HelloWorld.txt 的空文件
	file, err := os.Create("HelloWorld.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer file.Close()
}