package main

import "fmt"

// 写一个函数在原地完成消除[]string中相邻重复的字符串的操作。 写一个函数在原地完成消除[]string中相邻重复的字符串的操作。
func removeDuplicate(s []string) {
	// 直接在原 slice 上操作, 无需返回值
	for i := 0; i < len(s)-1; i++ {
		if s[i] == s[i+1] {
			// 删除重复的元素
			copy(s[i:], s[i+1:])
			// 重新切片
			s = s[:len(s)-1]
			i--
		}
	}
	fmt.Printf("去重后：%v\n", s)
}

func main() {
	var s = []string{"a", "b", "b", "c", "c", "c", "d", "e", "e", "f"}
	fmt.Printf("原始 slice：%v\n", s)
	removeDuplicate(s)
}
