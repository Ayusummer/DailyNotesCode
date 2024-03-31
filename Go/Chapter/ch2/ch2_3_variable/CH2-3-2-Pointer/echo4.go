// Echo4 prints its command-line arguments.
package main

import (
	"flag"
	"fmt"
	"strings"
)

var n = flag.Bool("n", false, "omit trailing newline") // 默认不省略换行符
var sep = flag.String("s", " ", "separator")

func main_echo4() {
	flag.Parse()
	fmt.Print(strings.Join(flag.Args(), *sep))
	if !*n {
		fmt.Println()
		fmt.Println()
		fmt.Println()
	}
}
