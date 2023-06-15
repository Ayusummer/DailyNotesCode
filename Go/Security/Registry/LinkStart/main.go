package main

import (
	"log"
	"os"
	"path/filepath"

	"golang.org/x/sys/windows/registry"
)

func main() {
	key, err := registry.OpenKey(registry.CURRENT_USER, `Software\Microsoft\Windows\CurrentVersion\Run`, registry.SET_VALUE)
	if err != nil {
		log.Fatal(err)
	}
	defer key.Close()

	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}

	exPath := filepath.ToSlash(ex)
	err = key.SetStringValue("MyApp", exPath)
	if err != nil {
		log.Fatal(err)
	}

	// 向当前目录写一个 HelloWorld.txt 的空文件
	f, err := os.Create("HelloWorld.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer f.Close()

}
