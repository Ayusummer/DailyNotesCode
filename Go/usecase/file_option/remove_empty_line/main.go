package main

import (
	"flag"
	"fmt"
)

func main() {
	filePath := flag.String("f", "", "需要删除空行的文件路径")
	help := flag.Bool("h", false, "显示帮助信息")

	flag.Parse()

	if *help {
		fmt.Printf("Usage: remove_empty_line -f <file_path>\n这将删除 <file_path> 文件中的空行并生成一个新文件 <file_path>.remove_empty_line 在其同级目录下\n")
		flag.PrintDefaults()
		return
	}

	if *filePath == "" {
		fmt.Println("请使用 -f <filepath>提供一个文件路径")
		return
	}

	RemoveEmptyLine(*filePath)
}
