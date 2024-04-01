package main

import (
	"encoding/json"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
)

// ipconfig.json 文件路径(默认为当前目录下的 ipconfig.json)
var ipconfigJSONPath string = "ipconfig.json"
var ipconfigMap map[string]string = readJsonFile(ipconfigJSONPath)

// 下载文件根目录(默认为当前目录下的 download 文件夹)
var downloadDir string = "download"

// 读取 ipconfig.json 文件
func readJsonFile(path string) map[string]string {
	file, err := os.Open(path)
	if err != nil {
		fmt.Println("Error:", err)
		return make(map[string]string)
	}
	defer file.Close()

	decoder := json.NewDecoder(file)
	info_map := make(map[string]string)
	err = decoder.Decode(&info_map)
	if err != nil {
		fmt.Println("Error:", err)
		return make(map[string]string)
	}
	return info_map
}

// 将 map 写回到 json 文件(直接覆盖原文件1)
func writeJsonFile(path string, info_map map[string]string) {
	file, err := os.Create(path)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer file.Close()

	encoder := json.NewEncoder(file)
	err = encoder.Encode(info_map)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

}

func handleIpconfig(w http.ResponseWriter, r *http.Request) {
	// 将传送过来的 json 数据插入到 ipconfigMap 中
	decoder := json.NewDecoder(r.Body)
	var newInfoMap map[string]string
	err := decoder.Decode(&newInfoMap)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	// fmt.Println(newInfoMap)
	for k, v := range newInfoMap {
		// fmt.Println("key:%s \n value:%s", k, v)
		// 打印 hostname 和 ip
		if k == "hostname" || k == "ip" {
			fmt.Printf("%s: %s\n", k, v)
		}
		ipconfigMap[k] = v
	}
	// 将 ipconfigMap 写回到 json 文件
	writeJsonFile(ipconfigJSONPath, ipconfigMap)
}

func downloadFile(w http.ResponseWriter, r *http.Request) {
	// 根据 query 参数 filename 获取文件名
	filename := r.URL.Query().Get("filename")
	fmt.Printf("正在下载文件: %s\n", filename)
	// 拼接 downloadDir 和 filename
	filepath := downloadDir + "/" + filename
	// 打开文件
	file, err := os.Open(filepath)
	if err != nil {
		fmt.Printf("下载文件失败, 读取文件 %s 失败: %s", filepath, err)
		return
	}
	defer file.Close()
	// 设置响应头
	w.Header().Set("filename", filename)
	w.Header().Set("Content-Type", "application/octet-stream")
	// 将文件写入到响应体
	_, err = io.Copy(w, file)
	if err != nil {
		fmt.Printf("下载文件失败, 写入响应体失败: %s", err)
		return
	}
}

func main() {
	http.HandleFunc("/ipconfig", handleIpconfig)
	http.HandleFunc("/download", downloadFile)
	log.Fatal(http.ListenAndServe(":8080", nil))
}
