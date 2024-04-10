package main

import (
	"fmt"
)

var c = "c"

func cc() {
	fmt.Printf("&c:%v, c:%s-cc()内部访问全局c\n", &c, c)
	c := "cc"
	fmt.Printf("&c:%v, c:%s-cc()内部简短变量声明屏蔽全局c\n", &c, c)
}

// func single_var_dup_assign() {
// 	a := "1"
// 	a := "2"	// 重复声明报错
// 	fmt.Printf("&a:%v, a:%s\n", &a, a)
// }

func single_var_scope_change() {
	a := "1"
	fmt.Printf("&a:%v, a:%s  -函数内\n", &a, a)
	for i := 0; i < 1; i++ {
		fmt.Printf("&a:%v, a:%s - for循环内部访问外层a\n", &a, a)
		a := "2"
		fmt.Printf("&a:%v, a:%s - for循环内部重新声明a\n", &a, a)
	}
}

func multi_var_dup_assign() {
	// a := "1"
	// b := "2"
	// a, b := "3", "4" // 重复声明报错

	a := "a"
	fmt.Printf("&a:%v, a:%s\n", &a, a)
	a, b := "b", "c"
	fmt.Printf("&a:%v, a:%s, &b:%v, b:%s\n", &a, a, &b, b)
}

func multi_var_dup_assign_scope_change() {
	a, b := "1", "2"
	fmt.Printf("&a:%v, a:%s, &b:%v, b:%s - 函数内部\n", &a, a, &b, b)
	for i := 0; i < 1; i++ {
		a, b := "2", "3"
		fmt.Printf("&a:%v, a:%s, &b:%v, b:%s - for循环内部\n", &a, a, &b, b)
	}
	fmt.Printf("&a:%v, a:%s, &b:%v, b:%s - 函数内部\n", &a, a, &b, b)

	// a := "a"
	// fmt.Printf("&a:%v, a:%s\n", &a, a)
	// for i := 0; i < 1; i++ {
	// 	fmt.Printf("&a:%v, a:%s - for循环内部访问外层a\n", &a, a)
	// 	a, b := "b", "c"
	// 	fmt.Printf("&a:%v, a:%s, &b:%v, b:%s - for循环内部\n", &a, a, &b, b)
	// }
	// fmt.Printf("&a:%v, a:%s - 函数内部\n", &a, a)

}

func main() {
	// a := "1"
	// fmt.Printf("&a:%v, a:%s\n", &a, a)
	// a, b := "2", "3"
	// fmt.Printf("&a:%v, a:%s, &b:%v, b:%s\n", &a, a, &b, b)
	// d := "d"
	// fmt.Printf("&b:%v, b:%s, &d:%v, d:%s  -main函数内\n", &b, b, &d, d)

	// for i := 0; i < 1; i++ {
	// 	a := "4"
	// 	fmt.Printf("&a:%v, a:%s - for循环内部\n", &a, a)
	// 	fmt.Printf("&b:%v, b:%s - for循环内部访问main中的bd\n", &b, b)
	// 	b, d, e := "5", "6", "7"
	// 	fmt.Printf("&b:%v, b:%s, &d:%v, d:%s, &e:%v, e:%s - for循环内部\n", &b, b, &d, d, &e, e)
	// }

	// fmt.Printf("&c:%v, c:%s-全局\n", &c, c)
	// cc()

	// 单一变量重复声明 - 作用域发生变化
	// single_var_scope_change()

	// 多变量重复声明
	// multi_var_dup_assign()

	// 多变量重复声明 - 作用域发生变化
	multi_var_dup_assign_scope_change()
}
