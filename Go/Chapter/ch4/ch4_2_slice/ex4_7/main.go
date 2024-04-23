package main

// reverse reverses a slice of ints in place.
func reverse(s []int) {
	for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
		s[i], s[j] = s[j], s[i]
	}
}

// 修改reverse函数用于原地反转UTF-8编码的[]byte。是否可以不用分配额外的内存？
func reverseUTF8(s []byte) {

}

func main() {

}
