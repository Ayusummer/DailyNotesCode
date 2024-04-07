// 重写PopCount函数，用一个循环代替单一的表达式。比较两个版本的性能。
package popcount

// pc[i] is the population count of i.
var pc [256]byte

func init() {
	// 这里的 for i:=range pc 只接收 range 返回的 index, value 中的 index, 也就是说 i 的值是 0-255
	for i := range pc {
		// go 语言中整数除法是向下取整的, 也就是说 1/2 = 0
		pc[i] = pc[i/2] + byte(i&1)
	}
}

// PopCount returns the population count (number of set bits) of x.
func PopCount(x uint64) int {
	var count int
	for i := 0; i < 8; i++ {
		count += int(pc[byte(x>>(uint(i)*8))])
	}
	return count
}
