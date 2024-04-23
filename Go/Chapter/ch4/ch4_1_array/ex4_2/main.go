// 编写一个程序，默认情况下打印标准输入的SHA256编码，并支持通过命令行flag定制，输出SHA384或SHA512哈希算法。
package main

import (
	"bufio"
	"crypto/sha256"
	"crypto/sha512"
	"flag"
	"fmt"
	"os"
)

// 计算数据的 SHA256 哈希码
func sha256Hash(data []byte) string {
	sha256 := sha256.Sum256(data)
	return fmt.Sprintf("%x", sha256)
}

// 计算数据的 SHA384 哈希码
func sha384Hash(data []byte) string {
	sha384 := sha512.Sum384(data)
	return fmt.Sprintf("%x", sha384)
}

// 计算数据的 SHA512 哈希码
func sha512Hash(data []byte) string {
	sha512 := sha512.Sum512(data)
	return fmt.Sprintf("%x", sha512)
}

var hashType = flag.String("ht", "sha256", "hashType-支持 sha256, sha384, sha512")

func main() {
	flag.Parse()

	hashType := *hashType

	// 如果输入的哈希类型不支持，则退出
	if hashType != "sha256" && hashType != "sha384" && hashType != "sha512" {
		fmt.Printf("不支持的哈希类型 %s\n", hashType)
		return
	}

	fmt.Printf("请输入需要计算 %s 哈希码的数据，输入 exit 退出\n", hashType)

	// 读取一行输入
	input := bufio.NewScanner(os.Stdin)
	for input.Scan() {
		// 遇到  exit 时退出
		if input.Text() == "exit" {
			break
		}

		data := input.Bytes()
		switch hashType {
		case "sha256":
			hash := sha256Hash(data)
			fmt.Println(hash[:])
		case "sha384":
			hash := sha384Hash(data)
			fmt.Println(hash[:])
		case "sha512":
			hash := sha512Hash(data)
			fmt.Println(hash[:])
		default:
			fmt.Printf("不支持的哈希类型 %s\n", hashType)
		}
	}
}
