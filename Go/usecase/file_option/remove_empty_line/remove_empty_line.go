// 删除一个文件中的空行
package main

import (
	"bufio"
	"fmt"
	"os"
)

func RemoveEmptyLine(filePath string) {
	// 读取文件
	file, err := os.Open(filePath)
	if err != nil {
		fmt.Println("无法打开文件:", err)
		panic(err)
	}
	defer file.Close()

	lines := make([]string, 0)
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if line != "" {
			lines = append(lines, line)
		}
	}

	// 写入文件, 源文件.remove_empty_line
	file, err = os.Create(filePath + ".remove_empty_line")
	if err != nil {
		fmt.Println("无法创建文件:", err)
		panic(err)
	}
	defer file.Close()

	for _, line := range lines {
		_, err := file.WriteString(line + "\n")
		if err != nil {
			fmt.Println("无法写入文件:", err)
			panic(err)
		}
	}

	fmt.Println("空行已删除, 新文件为:", filePath+".remove_empty_line")

}
