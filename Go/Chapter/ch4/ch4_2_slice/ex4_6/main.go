package main

import "fmt"

// 编写一个函数，原地将一个UTF-8编码的[]byte类型的slice中相邻的空格（参考unicode.IsSpace）替换成一个空格返回
func replaceSpace(s []byte) []byte {
	for i := 0; i < len(s)-1; i++ {
		if s[i] == ' ' && s[i+1] == ' ' {
			copy(s[i:], s[i+1:])
			s = s[:len(s)-1]
			i--
		}
	}
	return s
}

func main() {
	var s = []byte("a b  c   d    e")
	fmt.Printf("原始 slice：%v\n", string(s))
	s = replaceSpace(s)
	fmt.Printf("去除重复空格后：%v\n", string(s))
}
