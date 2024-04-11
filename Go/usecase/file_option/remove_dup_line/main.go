package main

import (
	"flag"
	"fmt"
)

func main() {
	// if len(os.Args) != 2 {
	// 	fmt.Println("请提供一个文件路径")
	// 	os.Exit(1)
	// }

	// // 命令行获取第一个参数作为文件路径
	// var filePath string = os.Args[1]

	filePath := flag.String("f", "", "需要删除重复行的文件路径")
	help := flag.Bool("h", false, "显示帮助信息")

	flag.Parse()

	if *help {
		fmt.Printf("Usage: remove_dup_line -f <file_path>\n这将删除 <file_path> 文件中的重复行并生成一个新文件 <file_path>.remove_dup_line 在其同级目录下\n")
		flag.PrintDefaults()
		return
	}

	if *filePath == "" {
		fmt.Println("请提供一个文件路径")
		return
	}

	RemoveDupLine(*filePath)

}
