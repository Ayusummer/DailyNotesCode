package linkstart

import (
	"fmt"
	"os"
	"os/exec"
	"syscall"
)

func WithCMD() {
	// 获取当前可执行文件的路径
	ex, err := os.Executable()
	if err != nil {
		fmt.Println(err)
		return
	}

	// 创建一个 *Cmd
	cmd := exec.Command("reg", "add", `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, "/v", "MyAppWriteHelloWorld", "/t", "REG_SZ", "/d", ex, "/f")

	// 获取一个新的进程属性
	attr := &syscall.SysProcAttr{HideWindow: true}

	// 将新的进程属性应用到 cmd
	cmd.SysProcAttr = attr

	// 运行 cmd
	err = cmd.Run()
	if err != nil {
		fmt.Println(err)
		return
	}

	// fmt.Println("Registry entry created")
	// 向当前目录写一个 HelloWorld.txt 的空文件
	f, err := os.Create("HelloWorld.txt")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer f.Close()
}
