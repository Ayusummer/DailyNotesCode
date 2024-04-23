// 编写一个函数，计算两个SHA256哈希码中不同bit的数目
package main

import "crypto/sha256"

// 比较两个 SHA256 哈希码中不同 bit 的数量
func diffBitCount(hash1, hash2 [32]byte) int {
	count := 0
	for i := 0; i < 32; i++ {
		// 异或操作，相同为 0，不同为 1
		diff := hash1[i] ^ hash2[i]
		diff_int := popCountUint8(diff)
		// 计算不同 bit 的数量
		count += diff_int
	}
	return count
}

// 计算一个 unit8 中 1 的数量
func popCountUint8(x uint8) int {
	count := 0
	for x != 0 {
		x = x & (x - 1)
		count++
	}
	return count
}

func main() {
	c1 := sha256.Sum256([]byte("x"))
	c2 := sha256.Sum256([]byte("X"))
	println(diffBitCount(c1, c2))
}
