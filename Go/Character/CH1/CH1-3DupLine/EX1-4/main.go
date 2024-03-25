package main

import (
	"bufio"
	"fmt"
	"os"
)

// 统计标准输入或文件中重复的行
func countLines(f *os.File, counts map[string]int) {
	input := bufio.NewScanner(f)
	for input.Scan() {
		// 遇到 -1 时, input.Scan() 退出循环
		if input.Text() == "-1" {
			break
		}
		counts[input.Text()]++
	}
	// 注意: 忽略input.Err()中可能的错误
}

// 读取标准输入或是使用 os.Open 打开各个具名文件，并操作它们
// 练习 1.4:  修改 dup2, 出现重复的行时打印文件名称
func Dup2_alter() {
	counts := make(map[string]int)
	files := os.Args[1:]
	if len(files) == 0 {
		countLines(os.Stdin, counts)
	} else {
		for _, arg := range files {
			f, err := os.Open(arg)
			if err != nil {
				fmt.Fprintf(os.Stderr, "dup2: %v\n", err)
				continue
			}
			countLines(f, counts)
			// 如果重复行数大于 1, 则打印文件名
			for line, n := range counts {
				if n > 1 {
					fmt.Printf("文件名: %s\t重复次数: %d\t重复行: %s\n", arg, n, line)
				}
			}
			f.Close()
		}
	}
}

func main() {
	Dup2_alter()
}
