/*
练习 1.9
修改 fetch 打印出HTTP协议的状态码，可以从 resp.Status 变量得到该状态码。
*/
package main

import (
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"strings"
)

func PrintResponseBody_Copy_Prefix_Status() {
	for _, url := range os.Args[1:] { // 遍历命令行参数中的每个URL
		// 如果输入的url参数没有 http:// 前缀的话，为这个url加上该前缀
		if !strings.HasPrefix(url, "http://") {
			url = "http://" + url
			fmt.Printf("输入的url参数没有 http:// 前缀,已为该url加上该前缀\n当前url为: %s\n", url)
		}
		resp, err := http.Get(url) // 发送HTTP GET请求并获取响应
		// 如果有错误发生，打印错误信息并退出程序并返回错误码1
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		defer resp.Body.Close() // 关闭响应体

		// 打印HTTP协议的状态码
		fmt.Printf("HTTP协议的状态码: %s", resp.Status)

		n, err := io.Copy(os.Stdout, resp.Body) // 读取响应体
		if err != nil {
			log.Fatal(err)
		}
		fmt.Printf("Copied %d bytes \n", n)
	}
}

func main() {
	PrintResponseBody_Copy_Prefix_Status()
}
