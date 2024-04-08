// 比较两个版本 PopCount函数的性能
package main

import (
	ex2_3_popcount "GoLearning/Chapter/ch2/ch2_6_package_and_file/ex2_3/popcount"
	ex2_4_popcount "GoLearning/Chapter/ch2/ch2_6_package_and_file/ex2_4/popcount"
	popcount "GoLearning/Chapter/ch2/ch2_6_package_and_file/popcount"
	"fmt"
	"time"
)

func main() {
	var popcount_value int
	var ex2_3_popcount_value int
	var ex2_4_popcount_value int

	start := time.Now()
	for i := 0; i < 1000000; i++ {
		popcount_value = popcount.PopCount(0x1234567890ABCDEF)
	}
	time_spent := time.Since(start).Nanoseconds()
	fmt.Printf("%-25s %v ns\n", "popcount.PopCount:", time_spent)

	start = time.Now()
	for i := 0; i < 1000000; i++ {
		ex2_3_popcount_value = ex2_3_popcount.PopCount(0x1234567890ABCDEF)
	}
	time_spent = time.Since(start).Nanoseconds()
	fmt.Printf("%-25s %v ns\n", "ex2_3_popcount.PopCount:", time_spent)

	start = time.Now()
	for i := 0; i < 1000000; i++ {
		ex2_4_popcount_value = ex2_4_popcount.PopCount(0x1234567890ABCDEF)
	}
	time_spent = time.Since(start).Nanoseconds()
	fmt.Printf("%-25s %v ns\n", "ex2_4_popcount.PopCount:", time_spent)

	fmt.Printf("%-25s %v\n", "popcount.PopCount:", popcount_value)
	fmt.Printf("%-25s %v\n", "ex2_3_popcount.PopCount:", ex2_3_popcount_value)
	fmt.Printf("%-25s %v\n", "ex2_4_popcount.PopCount:", ex2_4_popcount_value)

}
