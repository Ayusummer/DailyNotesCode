// 练习 1.10: 找一个数据量比较大的网站, 用本小节中的程序调研网站的缓存策略, 对每个URL执行两遍请求, 查看两次时间是否有较大的差别, 并且每次获取到的响应内容是否一致
// 修改本节中的程序, 将响应结果输出到文件, 以便于进行对比

package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
	"strings"
	"time"
)

func fetch(url string, ch chan<- string, suffix string) {
	start := time.Now()

	// Create file
	fileName := fmt.Sprintf("fetchall_%s_%s_%s.txt", url, time.Now().Format("20060102_150405"), suffix)
	fileName = strings.ReplaceAll(fileName, ":", "_")
	fileName = strings.ReplaceAll(fileName, "/", "_")
	fileName = strings.ReplaceAll(fileName, ".", "_")
	file, err := os.Create(fileName)
	if err != nil {
		ch <- fmt.Sprint(err) // send to channel ch
		return
	}

	resp, err := http.Get(url)
	if err != nil {
		ch <- fmt.Sprint(err) // send to channel ch
		return
	}

	// 将响应结果输出到文件
	nbytes, err := io.Copy(file, resp.Body)
	resp.Body.Close() // don't leak resources
	if err != nil {
		ch <- fmt.Sprintf("while reading %s: %v", url, err)
		return
	}
	secs := time.Since(start).Seconds()
	ch <- fmt.Sprintf("%.2fs  %7d  %s", secs, nbytes, url)

	file.WriteString(fmt.Sprintf("%.2fs  %7d  %s", secs, nbytes, url))
	defer file.Close()

}

func main() {
	start := time.Now()
	ch := make(chan string)
	for _, url := range os.Args[1:] {
		go fetch(url, ch, "1") // start a goroutine
		go fetch(url, ch, "2") // start a goroutine
	}
	for range os.Args[1:] {
		fmt.Println(<-ch) // receive from channel ch
		fmt.Println(<-ch) // receive from channel ch
	}
	fmt.Printf("%.2fs elapsed\n", time.Since(start).Seconds())
}
