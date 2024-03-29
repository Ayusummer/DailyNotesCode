package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 3 {
		fmt.Println("Usage: sender <receiverIP> <listenPort>")
		return
	}

	receiverAddr := os.Args[1]
	listenPort := os.Args[2]

	conn, err := net.Dial("udp", receiverAddr+":"+listenPort)
	if err != nil {
		fmt.Println("Error:", err)
		return
	} else {
		fmt.Println("Connected to", receiverAddr+":"+listenPort)
	}
	// main 函数结束才会关闭,而非此时就关闭了
	defer conn.Close()

	scanner := bufio.NewScanner(os.Stdin)
	for scanner.Scan() {
		message := scanner.Text()
		_, err := conn.Write([]byte(message))
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
	}

}
