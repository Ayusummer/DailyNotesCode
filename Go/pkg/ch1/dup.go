package ch1

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"os"
	"strings"
)

// 打印标准输入中多次出现的行, 以重复次数开头
func Dup1() {
	// 创建一个空的 map, 键为 string, 值为 int
	counts := make(map[string]int)
	// 创建一个从标准输入读取数据的 Scanner
	input := bufio.NewScanner(os.Stdin)
	// 逐行读取标准输入并更新 map counts
	for input.Scan() {
		// 遇到 0 时, input.Scan() 退出循环
		if input.Text() == "0" {
			break
		}
		counts[input.Text()]++

	}
	// 注意: 忽略input.Err()中可能的错误
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}

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
func Dup2() {
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
			f.Close()
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
}

// 一次性读取指定文件到内存中, 然后进行分割与计算重复行的操作
func Dup3() {
	counts := make(map[string]int)
	for _, filename := range os.Args[1:] {
		data, err := ioutil.ReadFile(filename)
		if err != nil {
			fmt.Fprintf(os.Stderr, "dup3: %v\n", err)
			continue
		}
		for _, line := range strings.Split(string(data), "\r\n") {
			counts[line]++
		}
	}
	for line, n := range counts {
		if n > 1 {
			fmt.Printf("%d\t%s\n", n, line)
		}
	}
	// 输出 counts 中的所有键值对
	fmt.Printf("---------------\n")
	for line, n := range counts {
		fmt.Printf("%d\t%s\n", n, line)
	}
}
