// 修改charcount程序，使用unicode.IsLetter等相关的函数，统计字母、数字等Unicode中不同的字符类别。

package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"unicode"
	"unicode/utf8"
)

func main() {
	counts := map[string]int{
		"letter":  0,
		"digit":   0,
		"space":   0,
		"punct":   0,
		"control": 0,
		"other":   0,
	}
	var utflen [utf8.UTFMax + 1]int // count of lengths of UTF-8 encodings
	invalid := 0                    // count of invalid UTF-8 characters

	in := bufio.NewReader(os.Stdin)

	for {
		r, n, err := in.ReadRune() // returns rune, nbytes, error
		if err == io.EOF {
			break
		}
		if err != nil {
			fmt.Fprintf(os.Stderr, "charcount: %v\n", err)
			os.Exit(1)
		}

		if r == utf8.RuneError && n == 1 {
			invalid++
			continue
		}
		switch {
		case unicode.IsLetter(r):
			counts["letter"]++
		case unicode.IsDigit(r):
			counts["digit"]++
		case unicode.IsSpace(r):
			counts["space"]++
		case unicode.IsPunct(r):
			counts["punct"]++
		case unicode.IsControl(r):
			counts["control"]++
		default:
			counts["other"]++
		}
		utflen[n]++

	}

	fmt.Printf("category\tcount\n")
	for c, n := range counts {
		fmt.Printf("%q\t%d\n", c, n)
	}
	fmt.Print("\nlen\tcount\n")
	for i, n := range utflen {
		if i > 0 {
			fmt.Printf("%d\t%d\n", i, n)
		}
	}
	if invalid > 0 {
		fmt.Printf("\n%d invalid UTF-8 characters\n", invalid)
	}
}
