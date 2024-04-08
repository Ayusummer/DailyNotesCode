// 表达式`x&(x-1)`用于将x的最低的一个非零的bit位清零。使用这个算法重写PopCount函数，然后比较性能。

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

// 表达式 x&(x-1) 用于将x的最低的一个非零的bit位清零。使用这个算法重写PopCount函数，然后比较性能。
func PopCount(x uint64) int {
	var count int
	for x != 0 {
		count++
		x &= x - 1
	}
	return count
}
