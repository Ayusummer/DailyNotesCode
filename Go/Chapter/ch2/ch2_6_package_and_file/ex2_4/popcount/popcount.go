// 用移位算法重写 `PopCount` 函数，每次测试最右边的1bit，然后统计总数
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

// 用移位算法重写 PopCount 函数，每次测试最右边的1bit，然后统计总数
func PopCount(x uint64) int {
	var count int
	for i := 0; i < 64; i++ {
		count += int(x & 1)
		x >>= 1
	}
	return count
}
