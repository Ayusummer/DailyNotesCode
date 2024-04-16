package main

import "fmt"

const (
	_  = 1 << (10 * iota) // iota在这里被重置为0
	KB                    // 1024
	MB                    // 1048576
	GB                    // 1073741824
	TB                    // 1099511627776
	PB                    // 1125899906842624
	EB                    // 1152921504606846976
)

func main() {
	fmt.Printf("KB: %d, MB: %d, GB: %d, TB: %d, PB: %d, EB: %d\n", KB, MB, GB, TB, PB, EB)
}
