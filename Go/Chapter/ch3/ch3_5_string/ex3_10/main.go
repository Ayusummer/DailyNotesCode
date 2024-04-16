package main

import (
	"bytes"
	"fmt"
)

func comma(s string) string {
	var buf bytes.Buffer
	n := len(s)
	if n <= 3 {
		return s
	}
	remainder := n % 3
	if remainder != 0 {
		buf.WriteString(s[:remainder])
		buf.WriteByte(',')
		s = s[remainder:]
	}
	for len(s) > 0 {
		buf.WriteString(s[:3])
		s = s[3:]
		if len(s) > 0 {
			buf.WriteByte(',')
		}
	}
	return buf.String()
}

func main() {
	var s = comma("123456789")
	fmt.Println(s)
}
