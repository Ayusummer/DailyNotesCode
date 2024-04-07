// 通用的单位转换程序,支持长度、重量、温度的单位转换;从命令行读取参数, 如果缺省的话则是从标准输入读取参数然后做相应的转换
package main

import (
	"GoLearning/Chapter/ch2/ch2_6_package_and_file/ex2_2/lengthconv"
	"GoLearning/Chapter/ch2/ch2_6_package_and_file/ex2_2/tempconv"
	"GoLearning/Chapter/ch2/ch2_6_package_and_file/ex2_2/weightconv"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var number string
	var unit string

	// 获取命令行参数
	if len(os.Args) > 1 {
		// 第一个参数为待转换的单位,例如: 100F, 100ft, 100lb
		number = os.Args[1]
		// 第二个参数为待转换的单位,例如: F, ft, lb
		unit = os.Args[2]
	} else {
		// 从标准输入读取参数
		fmt.Println("Please input the number and unit:")
		fmt.Scanln(&number, &unit)
	}

	// 将输入的数字转换为浮点数
	num, err := strconv.ParseFloat(number, 64)
	if err != nil {
		fmt.Fprintf(os.Stderr, "unitconv: %v\n", err)
		os.Exit(1)
	}

	// 根据输入的单位进行转换
	switch unit {
	case "°C":
		c := tempconv.Celsius(num)
		f := tempconv.CToF(c)
		k := tempconv.CToK(c)
		fmt.Printf("%s = %s, %s = %s\n", c, f, c, k)
	case "°F":
		f := tempconv.Fahrenheit(num)
		c := tempconv.FToC(f)
		k := tempconv.FToK(f)
		fmt.Printf("%s = %s, %s = %s\n", f, c, f, k)
	case "°K":
		k := tempconv.Kelvin(num)
		c := tempconv.KToC(k)
		f := tempconv.KToF(k)
		fmt.Printf("%s = %s, %s = %s\n", k, c, k, f)
	case "ft":
		f := lengthconv.Feet(num)
		m := lengthconv.FToM(f)
		fmt.Printf("%s = %s\n", f, m)
	case "m":
		m := lengthconv.Meter(num)
		f := lengthconv.MToF(m)
		fmt.Printf("%s = %s\n", m, f)
	case "lb":
		p := weightconv.Pound(num)
		k := weightconv.PToK(p)
		fmt.Printf("%s = %s\n", p, k)
	case "kg":
		k := weightconv.Kilogram(num)
		p := weightconv.KToP(k)
		fmt.Printf("%s = %s\n", k, p)
	default:
		fmt.Fprintf(os.Stderr, "unitconv: unknown unit %s\n", unit)
		os.Exit(1)
	}
}
