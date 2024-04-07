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
	return int(pc[byte(x>>(0*8))] +
		pc[byte(x>>(1*8))] +
		pc[byte(x>>(2*8))] +
		pc[byte(x>>(3*8))] +
		pc[byte(x>>(4*8))] +
		pc[byte(x>>(5*8))] +
		pc[byte(x>>(6*8))] +
		pc[byte(x>>(7*8))])
}
