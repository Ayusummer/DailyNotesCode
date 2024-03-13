package main

import "fmt"

// 指针赋值
func pointer_assign() {
	x := 1
	p := &x         // p, of type *int, points to x
	fmt.Println(*p) // "1"
	*p = 2          // equivalent to x = 2
	fmt.Println(x)  // "2"
}

// 判断地址是否相等
func address_equal() {
	var x, y int
	fmt.Println(&x == &x, &x == &y, &x == nil) // "true false false"
}

func f() *int {
	v := 1
	return &v
}

func incr(p *int) int {
	*p++ // 非常重要：只是增加p指向的变量的值，并不改变p指针！！！
	return *p
}

func main() {
	// pointer_assign()
	// address_equal()

	// var p = f()
	// fmt.Println(*p)         // "1"
	// fmt.Println(f() == f()) // "false"

	// v := 1
	// incr(&v)              // side effect: v is now 2
	// fmt.Println(incr(&v)) // "3" (and v is 3)

	main_echo4()

}
