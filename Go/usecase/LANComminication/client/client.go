package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: receiver <listenPort>")
		return
	}

	listenPort := os.Args[1]

	addr, err := net.ResolveUDPAddr("udp", ":"+listenPort)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	conn, err := net.ListenUDP("udp", addr)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}
	defer conn.Close()

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
