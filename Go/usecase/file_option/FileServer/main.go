// Go 文件服务器,
package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"io"
	"log"
	"net/http"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"time"
)

var (
	LogFile *os.File
	Logger  *log.Logger
)

// 定义 HTML 模板内容
const html = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>File Upload & Download</title>
</head>
<body>
    <h1>File Upload & Download</h1>

    <h2>Upload File</h2>
    <form id="uploadForm" action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" id="fileInput" required>
        <button type="submit">Upload</button>
    </form>

    <h2>Download File</h2>
    <ul id="fileList"></ul>

    <script>
        // 发送 AJAX 请求获取文件列表数据
        fetch('/fileList')
            .then(response => response.json())
            .then(data => {
                const fileListElement = document.getElementById('fileList');
                // 清空文件列表
                fileListElement.innerHTML = '';
                // 为每个文件创建超链接并添加到列表中
                data.forEach(file => {
                    const listItem = document.createElement('li');
                    const link = document.createElement('a');
                    link.textContent = file;
                    const fileName = file.split('/').pop(); // 文件名
                    link.href = '/download?file=' + encodeURIComponent(file);
                    // 设置下载链接的文件名
                    link.setAttribute('download', fileName);
                    listItem.appendChild(link);
                    fileListElement.appendChild(listItem);
                });
            });
    </script>
</body>
</html>
`

func uploadHandler(w http.ResponseWriter, r *http.Request) {
	// 获取源ip
	sourceIP := r.RemoteAddr
	// 获取当前时间
	currentTime := time.Now().Format("2006-01-02 15:04:05")

	// 解析上传的文件
	r.ParseMultipartForm(10 << 20) // 限制上传文件大小为10MB
	file, handler, err := r.FormFile("file")
	if err != nil {
		Logger.Printf("ERROR: [%s] [%s] 解析上传文件失败: %v \n", currentTime, sourceIP, err)
		return
	}
	defer file.Close()

	// 创建保存文件
	f, err := os.OpenFile("files/"+handler.Filename, os.O_WRONLY|os.O_CREATE, 0666)
	if err != nil {
		Logger.Printf("ERROR: [%s] [%s] 上传文件保存失败: %v \n", currentTime, sourceIP, err)
		return
	}
	defer f.Close()

	// 将上传的文件内容拷贝到保存文件中
	io.Copy(f, file)

	w.WriteHeader(http.StatusCreated)
	w.Write([]byte("File uploaded successfully"))
	Logger.Printf("INFO: [%s] [%s] 上传文件成功: %s \n", currentTime, sourceIP, handler.Filename)
}

func downloadHandler(w http.ResponseWriter, r *http.Request) {
	// 获取源ip
	sourceIP := r.RemoteAddr
	// 获取当前时间
	currentTime := time.Now().Format("2006-01-02 15:04:05")

	// 获取文件名
	fileName := r.URL.Query().Get("file")

	// 获取当前程序所在目录
	dir, err := os.Getwd()
	if err != nil {
		Logger.Printf("ERROR: [%s] [%s] 获取当前目录失败: %v \n", currentTime, sourceIP, err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	// 拼接文件路径
	filePath := filepath.Join(dir, "files", fileName)

	// 检查文件路径是否在files目录下
	if !strings.HasPrefix(filePath, filepath.Join(dir, "files")) {
		Logger.Printf("ERROR: [%s] [%s] 文件路径不在files目录下: %s \n", currentTime, sourceIP, filePath)
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	// 打开文件
	file, err := os.Open(filePath)
	if err != nil {
		Logger.Printf("ERROR: [%s] [%s] 打开文件失败: %v \n", currentTime, sourceIP, err)
		w.WriteHeader(http.StatusNotFound)
		return
	}
	defer file.Close()

	// 将文件内容拷贝到响应中
	_, err = io.Copy(w, file)
	if err != nil {
		Logger.Printf("ERROR: [%s] [%s] 读取文件内容失败: %v \n", currentTime, sourceIP, err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	Logger.Printf("INFO: [%s] [%s] 下载文件成功: %s \n", currentTime, sourceIP, fileName)
}

func init() {
	// 检查当前目录下是否存在 files 文件夹, 不存在则创建
	createDirectoryIfNotExist("files")

	// 检查当前目录下是否存在 logs 文件夹, 不存在则创建
	createDirectoryIfNotExist("logs")

	// 检查当前目录下是否有 index.html 文件, 不存在则创建, 并写入 HTML 模板内容
	if _, err := os.Stat("index.html"); os.IsNotExist(err) {
		err := os.WriteFile("index.html", []byte(html), 0644)
		if err != nil {
			log.Fatalf("Error creating index.html: %v", err)
		}
	}

	// 初始化日志
	initLog()
}

func initLog() {
	// 打开日志文件
	var err error
	LogFile, err = os.OpenFile("logs/GoFileServer.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalf("Error opening log file: %v", err)
	}

	// 创建一个新的日志记录器
	Logger = log.New(LogFile, "", log.LstdFlags)

	// 检查日志文件大小
	go checkLogFileSize()
}

func checkLogFileSize() {
	for {
		// 每分钟检查一次文件大小
		time.Sleep(time.Minute)

		// 获取文件信息
		info, err := LogFile.Stat()
		if err != nil {
			Logger.Printf("Error getting log file info: %v", err)
			continue
		}

		// 如果文件大小超过1M，存档并创建新的日志文件
		if info.Size() > 1<<20 {
			archiveLog()
		}
	}
}

func archiveLog() {
	// 关闭当前的日志文件
	LogFile.Close()

	// 重命名当前的日志文件
	os.Rename("logs/GoFileServer.log", fmt.Sprintf("logs/%dGoFileServer.log", time.Now().Unix()))

	// 创建新的日志文件
	var err error
	LogFile, err = os.OpenFile("logs/GoFileServer.log", os.O_RDWR|os.O_CREATE|os.O_APPEND, 0666)
	if err != nil {
		log.Fatalf("Error opening log file: %v", err)
	}

	// 创建新的日志记录器
	Logger = log.New(LogFile, "", log.LstdFlags)
}

func createDirectoryIfNotExist(dirName string) {
	if _, err := os.Stat(dirName); os.IsNotExist(err) {
		err := os.Mkdir(dirName, 0755)
		if err != nil {
			Logger.Fatalf("创建目录失败 %s: %v", dirName, err)
		}
	}
}

func indexHandler(w http.ResponseWriter, r *http.Request) {
	http.ServeFile(w, r, "index.html")
}

func fileListHandler(w http.ResponseWriter, r *http.Request) {
	// 获取文件列表
	files, err := getFileList("files")
	if err != nil {
		Logger.Printf("获取文件列表失败: %v", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	// 将文件列表以 JSON 格式返回给客户端
	json.NewEncoder(w).Encode(files)
}

func getFileList(dir string) ([]string, error) {
	var files []string

	// 扫描目录下的文件
	err := filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
		if err != nil {
			return err
		}
		if !info.IsDir() {
			// 获取相对路径
			relPath, err := filepath.Rel(dir, path)
			if err != nil {
				return err
			}
			// 修复 Windows 路径分隔符
			relPath = strings.ReplaceAll(relPath, "\\", "/")
			files = append(files, relPath)
		}
		return nil
	})
	if err != nil {
		return nil, err
	}

	return files, nil
}

var (
	host = flag.String("host", "0.0.0.0", "host to bind to")
	port = flag.Int("port", 8080, "port to listen on")
)

func main() {
	flag.Parse()

	http.HandleFunc("/", indexHandler)
	http.HandleFunc("/upload", uploadHandler)
	http.HandleFunc("/download", downloadHandler)
	http.HandleFunc("/fileList", fileListHandler)

	// 获取并保存当前进程的 PID
	pid := os.Getpid()
	err := os.WriteFile("server.pid", []byte(strconv.Itoa(pid)), 0644)
	if err != nil {
		log.Fatalf("Failed to write PID to file: %v", err)
	}

	address := fmt.Sprintf("%s:%d", *host, *port)
	Logger.Println("Server started at http://localhost:8080")
	Logger.Fatal(http.ListenAndServe(address, nil))
}
