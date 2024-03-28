// 练习 1.3: 做实验测量潜在低效的版本和使用了 strings.Join 的版本的运行时间差异
package main

import (
	"fmt"
	"os"
	"strings"
	"time"
)

// 类似于 echo, 默认分隔符为一个空格
func Print_cmd_args() {
	// 定义一个字符串切片, 用于存储命令行参数
	var getParams string
	// 分隔符为一个空格
	var sep string = " "
	// 第 0 个参数是程序名, 第 1 个参数才是实际传入的首个参数
	for i := 1; i < len(os.Args); i++ {
		getParams += os.Args[i] + sep
	}
	fmt.Println(getParams)
}

// 使用切片构造 echo 语句
func Echo_Slice() {
	var getParams, sep string
	sep = " "
	for _, arg := range os.Args[1:] {
		getParams += arg + sep
	}
	fmt.Println(getParams)
}

// 使用 strings.Join() 方法构造 echo 语句
func Echo_Join() {
	fmt.Println(strings.Join(os.Args[1:], " "))
}

// 不考虑输出格式, 直接打印 os.Args 切片
func Echo_direct_print_slice() {
	fmt.Println(os.Args[1:])
}

// 定义一个函数类型
type EchoFuncType func()

func CalcEchoTimeWithTimes(f EchoFuncType, times int) {
	// 获取当前时间
	start := time.Now()
	for i := 0; i < times; i++ {
		f()
	}
	fmt.Println("执行时间(ms):", time.Since(start).Milliseconds())
	fmt.Println("执行时间(ns):", time.Since(start).Nanoseconds())
}

// 定义一个函数用于执行一个函数并计算执行时间
func CalcEchoTime(f EchoFuncType) {
	// 获取当前时间
	start := time.Now()
	f()
	// 打印函数名(×). Go中没有python/java那种对象的概念, 没有 f.__name__ 类似的写法, 直接 f 会打印函数地址
	fmt.Println("函数内存地址:", f)
	// 获取执行时间, 精确到毫秒
	fmt.Println("执行时间(ms):", time.Since(start).Milliseconds())
	// 获取执行时间, 精确到纳秒
	fmt.Println("执行时间(ns):", time.Since(start).Nanoseconds())
}

// 执行多个函数指定次数, 并在最后统一打印执行时间对比
func CompareEchoFunsExecTime(times int, func_names []string, f ...EchoFuncType) {
	// 定义一个时间切片, 用于存储每个函数的执行时间
	var execTime []int64

	for _, v := range f {
		start := time.Now()
		// 执行函数 times 次
		for i := 0; i < times; i++ {
			v()
		}
		execTime = append(execTime, time.Since(start).Milliseconds())
	}
	fmt.Println("--------------------------------------------------")
	for i, v := range execTime {
		fmt.Printf("函数名: %-25v, 执行时间(ms): %v\n", func_names[i], v)
	}
}

func main() {
	// CalcEchoTime(Print_cmd_args)
	// CalcEchoTime(Echo_Slice)
	// CalcEchoTime(Echo_Join)
	// CalcEchoTime(Echo_direct_print_slice)
	// 比较多个函数执行时间
	// func_names := []string{"Print_cmd_args", "Echo_Slice", "Echo_Join", "Echo_direct_print_slice"}
	// CompareEchoFunsExecTime(1000000, func_names, Print_cmd_args, Echo_Slice, Echo_Join, Echo_direct_print_slice)
	start := time.Now()
	for i := 0; i < 10000; i++ {
		fmt.Println(strings.Join(os.Args[1:], " "))
	}
	// 获取执行时间, 精确到毫秒
	fmt.Println("执行时间(ms):", time.Since(start).Milliseconds())
}
