package main

import (
	"flag"
	"fmt"
	"log"
	"net"
	"os"
	"os/exec"
	"strconv"
	"syscall"
)

var (
	action = flag.String("action", "start", "action to perform (start|stop)")
	host   = flag.String("host", "0.0.0.0", "host to bind to")
	port   = flag.Int("port", 8080, "port to listen on")
)

func main() {
	flag.Parse()

	switch *action {
	case "start":
		startServer(*host, *port)
	case "stop":
		stopServer()
	default:
		log.Fatalf("Unknown action: %s", *action)
	}
}

func startServer(host string, port int) {
	// 先检查当前端口是否被占用, 如果被占用则告警并退出(同时解决了不会重复启动的问题)
	listener, err := net.Listen("tcp", fmt.Sprintf("%s:%d", host, port))
	if err != nil {
		log.Fatalf("Failed to listen on port %d: %v", port, err)
	}
	listener.Close()

	start_server_cmd := fmt.Sprintf("goFileServer.exe -host %s -port %d", host, port)
	cmd := exec.Command("cmd", "/C", start_server_cmd)
	cmd.SysProcAttr = &syscall.SysProcAttr{HideWindow: true}
	err = cmd.Start()
	if err != nil {
		log.Fatalf("Failed to start server: %v", err)
	}

	// Write the PID to a file
	err = os.WriteFile("loader.pid", []byte(strconv.Itoa(cmd.Process.Pid)), 0644)
	if err != nil {
		log.Fatalf("Failed to write PID to file: %v", err)
	}

	fmt.Println("Server started")
}

func stopServer() {
	// Read the PID from the file
	dataServer, err := os.ReadFile("server.pid")
	if err != nil {
		log.Fatalf("Failed to read PID from file: %v", err)
	}
	dataLoader, err := os.ReadFile("loader.pid")
	if err != nil {
		log.Fatalf("Failed to read PID from file: %v", err)
	}

	// Convert the PID to an integer
	pidServer, err := strconv.Atoi(string(dataServer))
	if err != nil {
		log.Fatalf("Failed to convert PID to integer: %v", err)
	}
	pidLoader, err := strconv.Atoi(string(dataLoader))
	if err != nil {
		log.Fatalf("Failed to convert PID to integer: %v", err)
	}

	// Kill the processes
	killProcess(pidServer)
	killProcess(pidLoader)

	fmt.Println("Server stopped")
}

func killProcess(pid int) {
	process, err := os.FindProcess(pid)
	if err != nil {
		log.Fatalf("Failed to find process: %v", err)
	}

	err = process.Kill()
	if err != nil {
		log.Fatalf("Failed to kill process: %v", err)
	}
}
