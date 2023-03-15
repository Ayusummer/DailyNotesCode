package ch1

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func PrintResponseBody() {
	for _, url := range os.Args[1:] { // 遍历命令行参数中的每个URL
		resp, err := http.Get(url) // 发送HTTP GET请求并获取响应
		// 如果有错误发生，打印错误信息并退出程序并返回错误码1
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: %v\n", err)
			os.Exit(1)
		}
		b, err := io.ReadAll(resp.Body) // 读取响应体
		resp.Body.Close()               // 关闭响应体
		if err != nil {
			fmt.Fprintf(os.Stderr, "fetch: reading %s: %v\n", url, err)
			os.Exit(1)
		}
		fmt.Printf("%s", b) // 打印响应体
	}

}
