package main

import (
	"bufio"
	"fmt"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 4 {
		fmt.Println("Usage: program <localPort> <remoteAddr> <remotePort>")
		return
	}

	localPort := os.Args[1]
	remoteAddr := os.Args[2]
	remotePort := os.Args[3]

	lAddr, err := net.ResolveUDPAddr("udp", ":"+localPort)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	rAddr, err := net.ResolveUDPAddr("udp", remoteAddr+":"+remotePort)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	conn, err := net.DialUDP("udp", lAddr, rAddr)
	if err != nil {
		fmt.Println("Error:", err)
		return
	} else {
		fmt.Println("Connected to", remoteAddr+":"+remotePort)
	}
	// main 函数结束才会关闭,而非此时就关闭了
	defer conn.Close()

	go func() {
		scanner := bufio.NewScanner(os.Stdin)
		for scanner.Scan() {
			message := scanner.Text()
			_, err := conn.Write([]byte(message))
			if err != nil {
				fmt.Println("Error:", err)
				return
			}
		}
	}()

	buffer := make([]byte, 1024)
	for {
		n, _, err := conn.ReadFromUDP(buffer)
		if err != nil {
			fmt.Println("Error:", err)
			return
		}
		message := string(buffer[:n])
		fmt.Println("Received message:", message)
	}
}
