// 删除当前程序所在目录及子目录中指定名称的文件(需求来源于删除企微同步文件.WeDrive)
package main

import (
	"log"
	"os"
	"path/filepath"
)

func main() {
	targetFile := ".WeDrive"
	if len(os.Args) > 1 {
		targetFile = os.Args[1]
	}

	err := filepath.Walk(".", func(path string, info os.FileInfo, err error) error {
		if err != nil {
			log.Printf("prevent panic by handling failure accessing a path %q: %v\n", path, err)
			return err
		}

		if info.Name() == targetFile && !info.IsDir() {
			err := os.Remove(path)
			if err != nil {
				log.Printf("failed to delete file %q: %v\n", path, err)
				return err
			}
		}
		return nil
	})

	if err != nil {
		log.Printf("error walking the path .: %v\n", err)
	}
}
