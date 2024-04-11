// 删除一个文件中的重复行
package main

import (
	"bufio"
	"fmt"
	"os"
)

func RemoveDupLine(filePath string) {
	// 读取文件
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("无法打开文件:", err)
		panic(err)
	}
	defer file.Close()

	lines := make(map[string]bool)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if !lines[line] {
			// fmt.Println(line)
			lines[line] = true
		}
	}

	if err := scanner.Err(); err != nil {
		fmt.Println("读取文件时出错:", err)
	}

	// 写入文件, 源文件.remove_dup_line
	file, err = os.Create(filePath + ".remove_dup_line")
	if err != nil {
		fmt.Println("无法创建文件:", err)
		panic(err)
	}
	defer file.Close()

	for line := range lines {
		_, err := file.WriteString(line + "\n")
		if err != nil {
			fmt.Println("无法写入文件:", err)
			panic(err)
		}
	}

	fmt.Println("重复行已删除, 新文件为:", filePath+".remove_dup_line")

}
