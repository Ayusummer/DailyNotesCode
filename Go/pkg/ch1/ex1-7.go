/*
练习 1.7：

函数调用io.Copy(dst, src)会从src中读取内容，并将读到的结果写入到dst中，
使用这个函数替代掉例子中的 ioutil.ReadAll 来拷贝响应结构体到 os.Stdout，避免申请一个缓冲区（例子中的b）来存储。
记得处理io.Copy返回结果中的错误。
*/
package ch1

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

func PrintResponseBody_Copy() {
	for _, url := range os.Args[1:] { // 遍历命令行参数中的每个URL
		resp, err := http.Get(url) // 发送HTTP GET请求并获取响应
		// 如果有错误发生，打印错误信息并退出程序并返回错误码1
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		defer resp.Body.Close() // 关闭响应体

		n, err := io.Copy(os.Stdout, resp.Body) // 读取响应体
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("Copied %d bytes", n)
		log.Printf("Copied %d bytes", n)
		fmt.Printf("Copied %d bytes", n)
	}
}
