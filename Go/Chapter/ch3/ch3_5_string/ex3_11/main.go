package main

import (
	"bytes"
	"strings"
)

func comma(s string) string {
	var buf bytes.Buffer
	// 处理正负号
	if s[0] == '+' || s[0] == '-' {
		buf.WriteByte(s[0])
		s = s[1:]
	}
	// 处理浮点数
	dotIndex := strings.Index(s, ".")
	if dotIndex != -1 {
		buf.WriteString(commaInt(s[:dotIndex]))
		buf.WriteByte('.')
		buf.WriteString(s[dotIndex+1:])
	} else {
		buf.WriteString(commaInt(s))
	}
	return buf.String()
}

// 处理整数部分的逗号
func commaInt(s string) string {
	var buf bytes.Buffer
	n := len(s)
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
	var s = comma("123456789.123456")
	println(s)
	var s2 = comma("+123456789.123456")
	println(s2)
	var s3 = comma("-123456789.123456")
	println(s3)
}
